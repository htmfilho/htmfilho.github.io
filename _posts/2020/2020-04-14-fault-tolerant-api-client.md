---
layout: post
title:  "Circuit Breaker For API Calls in Java"
date: 2020-04-14 12:00:00 +0200
categories: java circuitbreaker api
---

![Tin Can Telephone](/images/posts/unreliable-api-call.png)

The life of system engineers would be a lot easier if they could squeeze all computing needs in a single computing unit. Reality is tougher. The complexity of systems is broken down into several components, some of them so resource intensive that they require their own computing instances. Multiple instances bring the communication of electronic devices to the table and there are countless things that can go wrong there. Good system design is the realization that those things should be handled gracefully, according to the rules of a discipline known as [Fault Tolerance].

<!-- more -->

Consider two business applications that interact through a web API. One application performs currency conversions and the other one uses this service to show the price of investment assets in the currency of the country where the customer resides. From the customer perspective, what would happen if the connection between the two applications is interrupted? Keeping the capability of trading assets is critical for the business, thus a graceful way to handle the unavailability of the currency converter is to show to customers prices in the currency where the asset is traded. Assets in a US stock exchange would be shown in USD. In Belgium, it would be shown in EUR.

What would trigger this behavioural change, also known as [graceful degradation]? A mechanism should be in place to automatically adapt to predictable circumstances maintaining the service operational with limited functionalities. If an application is calling a web API, it is easy to predict that the API might be unavailable at some point in time and the application should be ready to switch to a plan B.

The Java code below is a simple implementation of the [circuit breaker] pattern to change the application behaviour if the API call is not successful after a few attempts. It wraps the API call, watching for failures, and once the failures reach a certain threshold, the circuit opens, no further calls are made at that point, and the flow changes to do something else. Follow the documentation in the code to understand the logic.

{% highlight java %}
package ...;

import java.util.ArrayList;
import java.util.List;
import org.slf4j.Logger;

/**
 * Implementation of the circuit breaker pattern for logic that
 * involves API calls.
 * */
public class EndpointRetry {
    // Default thresholds
    public static final int DEFAULT_MAX_ATTEMPTS = 3;
    public static final long DEFAULT_WAITING_TIME = 300; // milliseconds

    /* While the thresholds are not reached, success determines the moment
       to stop. */
    private boolean success;

    /* Controls the number of attempts according to the threshold. */
    private int numAttemptsLeft;

    /* Time waiting between calls. */
    private long waitingTime;

    /* Keep track of the causes of the attempts. */
    private List<RuntimeException> failedAttemptCauses;

    /* The final exception that is thrown to change the behaviour. */
    private RuntimeException finalException;

    /**
     * Creates instance with the default thresholds.
     */
    public EndPointRetry() {
        this(DEFAULT_MAX_ATTEMPTS, DEFAULT_WAITING_TIME);
    }

    /**
     * Creates instance with custom thresholds.
     */
    public EndPointRetry(int numMaxAttempts, long waitingTime) {
        this.numAttemptsLeft = numMaxAttempts;
        this.waitingTime = waitingTime;
        this.failedAttemptCauses = new ArrayList<>(numMaxAttempts);
    }

    /**
     * The application can specify the final exception only once.
     */
    public void setFinalException(RuntimeException finalException) {
        if(finalException == null) {
            this.finalException = finalException;
        }
    }

    /**
     * Test to verify whether is necessary to retry or not.
     */
    public boolean retry() {
        boolean doRetry = !success && numAttemptsLeft > 0;
        success = true;
        return doRetry;
    }

    private void waitUntilNextAttempt() {
        try {
            Thread.sleep(waitingTime);
        } catch (InterruptedException ie) {
            throw new RuntimeException("Fail waiting for the next call");
        }
    }

    /**
     * Accumulate the causes and change state to eventually stop trying.
     * The accumulation is necessary because each failure can have a
     * different cause.
     * */
    public void errorOccurred(RuntimeException cause) {
        this.success = false;
        if (numAttemptsLeft <= 0) {
            this.finalException = new RuntimeException(
                String.format("%d attempts done every %d ms failed.",
                              numAttemptsLeft, waitingTime);
        }
        this.numAttemptsLeft--;
        waitUntilNextAttempt();
        failedAttemptCauses.add(cause);
    }

    /**
     * Put all the causes in the log to prevent interrupting the execution
     * during the attempts and throws a final exception to allow the caller
     * decide how to handle the situation.
     * */
    public void throwPossibleCauses(Logger logger) {
        if(failedAttemptCauses.size() > 0) {
            int i = 1;
            for (RuntimeException runtimeException : failedAttemptCauses) {
                logger.error("Attempt #" + i++, runtimeException);
            }
            throw finalException;
        }
    }
}
{% endhighlight %}

This is a simple implementation that targets API calls. It may need to be adapted to deal with files, databases, messaging services, and other connections that require fault tolerance. For a more generic solution, consider adopting an existing library such as [Netflix Hystrix][Hystrix]and [Resilience4j](https://resilience4j.readme.io).

Now, let's see how to use it. The code below calls an endpoint:

{% highlight java %}
private BigDecimal convertToCurrency(BigDecimal value, Currency currency) {
    EndpointRetry endpointRetry = new EndpointRetry();
    BigDecimal convertedValue = null;

    while (endpointRetry.retry()) {
        try {
            // Code to initialize the HTTP call, call the API and define the
            // variable convertedValue.

            if (responseCode != HttpURLConnection.HTTP_OK) {
                endpointRetry.setFinalException(
                  new AppException(
                      String.format("Not possible to convert %d to %s",  
                                    value, currency)));
            }
        } catch (MalformedURLException mfue) {
            throw new RuntimeException(String.format(
                "Configured URL is not well-formed: %s", url), mfue);
        } catch (SocketTimeoutException ste) {
            endpointRetry.errorOccurred(new RuntimeException(
                String.format("Timeout occurred accessing: %s", url), ste));
        } catch (IOException ie) {
            endpointRetry.errorOccurred(new RuntimeException(
                String.format("Service is unavailable: %s", url), ie));
        }
    }

    try {
        endpointRetry.throwPossibleCauses(LOG);
    } catch {
        return value;
    }
    return convertedValue;
}
{% endhighlight %}

Please, let me know your experience using this implementation and which improvements you made on top of it.

[circuit breaker]: https://martinfowler.com/bliki/CircuitBreaker.html

[Fault Tolerance]: https://en.wikipedia.org/wiki/Fault_tolerance

[graceful degradation]: https://www.sciencedirect.com/topics/computer-science/graceful-degradation

[Hystrix]: https://github.com/Netflix/Hystrix
