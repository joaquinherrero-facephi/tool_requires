# Issue tool_requires

Description

Using a tool_require 'tool' for all packages except for the 'tool' it hangs forever if a dependency of tool is missing.

In the example we use fmt as shared to force the build missing, otherwise it won't be missing and all will work properly.

Maybe conan install should detect this scenarios and raise an exception instead of silently hangup

On the other hand, there should be a mechanism to use the tool_require only when available (all deps already built)?

Code to reproduce:

```code
chmod +x run.sh
./run.sh
```

Env info:
```
Macos 14.3.1
Conan 2.1.0
Python 3.10.4
``````
