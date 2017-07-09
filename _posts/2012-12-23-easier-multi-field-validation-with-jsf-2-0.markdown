---
layout: post
title: "Easier Multi-Field Validation with JSF 2.0"
date: 2012-12-23 17:25:00 +0200
categories: uncategorized enterprise application java java ee jsf user interface web
---

One of the most frequent needs when developing application forms is multi-field validation (or cross-field, but I’m not using this term because when I put it on Google I actually got some post-war pictures). I’m talking about situations where we need to compare whether an initial date is earlier than an end date or a value is lower than another one. Isn’t it an obvious feature in every business-oriented framework? Not really. Unfortunately, the JSF specification doesn’t support it by default. Therefore, until its latest production release (<a href="http://www.jcp.org/en/jsr/detail?id=245" target="_blank">JSR 245</a> – JSF 2.1), JSF did not offer an out-of-the-box multi-field validation feature.

We probably can hope for something coming in JSF 2.2, since the <a href="http://jcp.org/en/jsr/detail?id=344" target="_blank">JSR 344</a> mentions “Multi-field validation”. Meanwhile, developers have used their fruitful creativity to implement their solutions. You can find plenty of working alternatives at <a href="http://stackoverflow.com/questions/6282466/jsf2-0-doesnt-support-cross-field-validation-is-there-a-workaround" target="_blank">Stackoverflow.com</a>; people creating their <a href="http://pawelstawicki.blogspot.be/2010/12/jsf20-component-for-cross-field.html" target="_blank">own components</a>; <a href="http://ocpsoft.org/java/jsf-2-0-cross-field-form-validation-simpl-in-reality/" target="_blank">frameworks built on top of Java EE</a> trying to cover this feature; and many other cases.

I didn’t like any solution I found. Some are complex, others are not so elegant. So, I decided to be creative as well and try a simpler solution, easy to understand and change when the time for refactoring comes. It doesn’t mean that I’m proposing something better than other proposals. I’m just proposing something simpler.

In the following example, I check whether an allocated budget is smaller than a budget limit. If not, then a message is shown to the user. The example considers only two fields, but it can scale to as many fields as you wish.

<h4>Step 1: create an attribute in the managed bean for each field to be validated:</h4>

The attributes below are exclusively used in the multi-field validation.

```
private BigDecimal validationAllocatedBudget;
private BigDecimal validationBudgetLimit;
```

In this example, I’m coding inside a class named MBean, annotated with @ManagedBean and @RequestScoped.

<h4>Step 2: create a validation method in the same managed bean for each field</h4>
This solution considers validation methods implemented in the managed bean instead of implementations of the interface <a href="http://docs.oracle.com/cd/E17802_01/j2ee/javaee/javaserverfaces/2.0/docs/api/javax/faces/validator/Validator.html">javax.faces.validator.Validator</a>.  You can give any name to validation methods as long as you define three standard parameters, which are the FacesContext, the UIComponent, and an Object representing the value input in the field. Only the value is useful for our validation. See the validation methods:

```
public void validateAllocatedBudget(FacesContext context,
                                    UIComponent component,
                                    Object value) {
    this.validationAllocatedBudget = (BigDecimal) value;
}

public void validateBudgetLimit(FacesContext context,
                                UIComponent component,
                                Object value) {
    this.validationBudgetLimit = (BigDecimal) value;
    if(this.validationBudgetLimit
             .compareTo(this.validationAllocatedBudget) < 0) {
       throw new ValidatorException(
         new FacesMessage("Invalid allocated budget!");
    }
}
```
