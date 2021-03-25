---
layout: post
title: "How a Python Script Can Launch a Clojure Application"
date: 2017-01-07 11:38:53 +0200
categories: development clojure python
---

If you ever need a Python Script that starts a Clojure application, do something else and then stops the application then this post is for you. The script below considers that you have a Clojure application that is self-contained in a single jar file. All the dependencies are there and you run it using `java -jar [jar-file.jar]`. If you have something different from that, then make sure the Clojure application can run via console from where the Python script is located. Learn the code below by reading the inline comments.

{% highlight python %}
# Copy, paste and adapt this code in a file located in the root of your Clojure project, in the same level of the project.clj file.
import os
import signal
import subprocess
import time
import traceback

# Reusable function used to kill a subprocess whenever needed. It is used twice in the code.
def _kill_subprocess(subp):
    os.killpg(os.getpgid(subp.pid), signal.SIGTERM)

# If you want, you can even build your self-contained jar file before executing it.
subprocess.call(['lein', 'ring', 'uberjar'])

# Executes the jar file as a subprocess, so it will be alive as long as the Python script keeps executing.
subp = subprocess.Popen(
    'java -jar target/proj-0.1.0-standalone.jar',
    shell=True,
    preexec_fn=os.setsid)

# Waits the application to fully launch before doing something else. You have to adapt the seconds below for the needs of your application.
time.sleep(12)

# Write some Python code that does something while the Clojure application is running. When it finishes then the Clojure application will also finish.
try:
    do_something_important()
except:
    traceback.print_exc()
    _kill_subprocess(subp)
    exit(1)

# Kills the subprocess to stop the Clojure application.
_kill_subprocess(subp)
exit(0)
{% endhighlight %}

That’s a use case, but if you need something slightly different from that let me know in the comments below.
