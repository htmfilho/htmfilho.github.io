---
layout: post
title: "Easier Multi-Field Validation with JSF 2.0"
date: 2012-12-23 17:25:00 +0200
categories: uncategorized enterprise application java java ee jsf user interface web
---

One of the most frequent needs when developing application forms is multi-field validation (or cross-field, but I'm not using this term because when I put it on Google I actually got some post-war pictures). I'm talking about situations where we need to compare whether an initial date is earlier than an end date or a value is lower than another one. Isn't it an obvious feature in every business-oriented framework? Not really. Unfortunately, the JSF specification doesn't support it by default. Therefore, until its latest production release (JSR 245 - JSF 2.1), JSF did not offer an out-of-the-box multi-field validation feature.

We probably can hope for something coming in JSF 2.2, since the JSR 344 mentions "Multi-field validation". Meanwhile, developers have used their fruitful creativity to implement their solutions. You can find plenty of working alternatives at Stackoverflow.com; people creating their own components; frameworks built on top of Java EE trying to cover this feature; and many other cases.

I didn't like any solution I found. Some are complex, others are not so elegant. So, I decided to be creative as well and try a simpler solution, easy to understand and change when the time for refactoring comes. It doesn't mean that I'm proposing something better than other proposals. I'm just proposing something simpler.

In the following example, I check whether an allocated budget is smaller than a budget limit. If not, then a message is shown to the user. The example considers only two fields, but it can scale to as many fields as you wish.

### Step 1: create an attribute in the managed bean for each field to be validated:

The attributes below are exclusively used in the multi-field validation.

{% highlight java %}
private BigDecimal validationAllocatedBudget;
private BigDecimal validationBudgetLimit;
{% endhighlight %}

In this example, I'm coding inside a class named MBean, annotated with `@ManagedBean` and `@RequestScoped`.

### Step 2: create a validation method in the same managed bean for each field

This solution considers validation methods implemented in the managed bean instead of implementations of the interface javax.faces.validator.Validator.  You can give any name to validation methods as long as you define three standard parameters, which are the FacesContext, the UIComponent, and an Object representing the value input in the field. Only the value is useful for our validation. See the validation methods:

{% highlight java %}
public void validateAllocatedBudget(FacesContext context,
                       UIComponent component, Object value) {
  this.validationAllocatedBudget = (BigDecimal) value;
}

public void validateBudgetLimit(FacesContext context,
                        UIComponent component, Object value) {
  this.validationBudgetLimit = (BigDecimal) value;
  if(this.validationBudgetLimit
          .compareTo(this.validationAllocatedBudget) < 0) {
    throw new ValidatorException(
      new FacesMessage("Invalid allocated budget!");
  }
}
{% endhighlight %}

The method validateAllocatedBudget doesn't validate the allocated budget. It simply set the attribute validationAllocatedBudget to allow its value to be used afterwards. It is possible because the validation methods are called in the same sequence they are declared in the JSF code. So, you can create a simple method like that for each field involved in the validation. The effective validation occurs in the method validateBudgetLimit, which is the latest called validation method in the JSF file, thus the last one to execute.

It's a good idea to declare attributes and validation methods in the same order of the fields in the form. The order doesn't interfere the functioning of the algorithm, but it helps to understand the logic. On the other hand, the order of calls in the JSF file is important.

### Step 3: use the parameter validator to reference the validation method

The methods described above are called from the fields below. Remember that the attributes and methods were implemented in the class MBean.

{% highlight xml %}
<h:outputLabel for="allocBudget" value="Allocated Budget"/>
<h:inputText id="allocBudget" label="Allocated Budget"
    value="#{mBean.operation.allocatedBudget}"
    validator="#{mBean.validateAllocatedBudget}"/>

<h:outputLabel for="budgetLimit" value="Budget Limit"/>
<h:inputText id="budgetLimit" label="Budget Limit"
    value="#{mBean.operation.budgetLimit}"
    validator="#{mBean.validateBudgetLimit}"/>
{% endhighlight %}

That's it! :) Merry Christmas and Happy New Year! \o/
