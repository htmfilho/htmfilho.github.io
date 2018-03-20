Write the test, write the code to pass the test and refactor.

{% highlight clojure %}
(ns minimily.utils.database-test
  (:require [clojure.test :refer :all]
            [minimily.utils.database :refer :all]))

(deftest test-mandatory-datasource-options
  (testing "The mandatory datasource options are present."
    (is (contains? options :adapter))
    (is (contains? options :server-name))
    (is (contains? options :port-number))
    (is (contains? options :database-name))
    (is (contains? options :username))
    (is (contains? options :password))))
{% endhighlight %}

    $ lein test    

    lein test minimily.utils.database-test

    Ran 1 tests containing 6 assertions.
    0 failures, 0 errors.

DRY principle: Don't repeat yourself. From functional to better functional.

{% highlight clojure %}
(deftest test-mandatory-datasource-options
  (testing "The mandatory datasource options are present."
    (is (reduce #(and %1 %2)
                (map #(contains? options %)
                     [:adapter :server-name :port-number :database-name
                      :username :password])))))
{% endhighlight %}

    $ lein test    

    lein test minimily.utils.database-test

    Ran 1 tests containing 1 assertions.
    0 failures, 0 errors.

It is not that the code lost readability. It is because to read it, it is necessary to learn the functional paradigm.

196 characteres to 113 characteres = 83 less
