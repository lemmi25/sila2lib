# SmartTemplate

This is a copy of Timm Severin's [SmartTemplate package](https://gitlab.com/tseverin/smart_template) (Version 0.2.1). 
It is included in sila2library to remove the external dependancy.

This package allows to replace template variables from a string template. It is heavily based on 
Pythons builtin `string.Template` class, however does not derive from it but is a standalone class.

Compared to the builtin implementation it also allows to execute functions (*hooks*) on the template
variables, which allows to re-use variables in the template, but adapt them to the current needs (e.g.
indentation, capitalisation, ...).

For a documentation of the code please refer to the corresponding [GitLab Pages](https://tseverin.gitlab.io/smart_template/docs/)

The general usage:

```python
from smart_template.smart_template import SmartTemplate

template_string = 'Hello $who_to_greet !' 

template =  SmartTemplate(template_string)

print(template.substitute(who_to_greet='World'))
# will print "Hello World !"
``` 

## Template variables

### In the template

There are two ways of specifying template variables in the template string:

```
$template_var
${template_var}
```

Both lead to the identical result, however, the second variant allows text to appear immediately 
after the template variables: 

```python
from smart_template.smart_template import SmartTemplate

# Goal:
#   replace <any>Class with SubClass 

# this will fail, since it cannot distinguish between the identifier and the following text
template_string = '$anyClass'
template = SmartTemplate(template_string)
template.substitute(any='Sub')  # -> KeyError: anyClass  

# if we use braces however, this is clear
template_string = '${any}Class'
template = SmartTemplate(template_string)
template.substitute(any='Sub')  # -> returns 'SubClass'
```

if you actually want to put a `$` in the text, use the character twice as escape character: `$$`.

### Passing to `smart_template`

There are two ways to pass template variables to the `SmartTemplate` object: As a dictionary or as
keyword/value pairs.
Both methods can be combined in the same call, however there can only ever be one dictionary passed, 
so when multiple dictionaries are to be used these must be merged first.

Example:
```python
template_string = '${first} ${second} ${third}'
template = SmartTemplate(template_string)
template.substitute({'first': 1, 'third': 3}, second=2)
```

This can be especially useful when you define your own function which creates a dictonary of 
replacement variables, but want to allow the user to also give keyword/value pairs:

```python
def my_own_function(**kwargs):
    
    import sys
    template_vars = {
        'version_major': sys.version_info.major,
        'version_minor': sys.version_info.minor,
        'version_micro': sys.version_info.micro
    }
    
    # ... perform further actions, create the template
    template.substitute(template_vars, **kwargs)
```

## Hooks

Hooks allow to change the value of a template variable in-place. The effectively pass the value of
the template variable to a function. Hooks are specified by pre-pending a template variable by the 
name of a hook, followed by a colon:

```
${hook:template_var}
```

You can chain a (nearly) arbitrary number of hooks. The code

```
${hook_2:hook_1:template_var}
```

will first execute `hook_1` on `template_var`, and then use the result with `hook_2` (*Note*: hooks 
are executed right to left!).

Some hooks can also accept function arguments. These must be passed in parentheses and separated by
commas.

```
${hook(arg_1,arg_2):template_var}
```

In the default version of the class no hooks are available. These need to be registered first.

### Register a hook

To register a hook the `SmartTemplate` class exposes the `add_function_hook()` method. This 
method expects a name for the hook and a function to call when the hook is found inside a template. 
It also accepts an optional third argument, that explains hwo the function arguments are to be 
interpreted.

The **name** must be passed as a string and should only contain alphanumeric characters and underscores, 
and must start with an underscore or a letter (see below).

The **func**tion passed must accept at least one argument, with the first argument being the value 
of the template variable that is to be modified. Further arguments can be allowed, either mandatory
or optional.

Example:

```python
# an identity hook, that does nothing
def hook_identity(input_string):
    return input_string
SmartTemplate.add_function_hook('identity', hook_identity)

# a hook that adds to strings together
def hook_append_text(input_string, append_string='_sub'):
    return input_string + append_string
# register without information on the argument(s)
SmartTemplate.add_function_hook('append', hook_append_text)
```

With this method we have defined a hook called `identity`, which does absolutely nothing and 
accepts no arguments, and a hook called `append`  that accepts zero or one argument. We can call 
these from the template:

```
# $template_var = 'Class'
Identity ${identity:template_var}                   # Output: Class
Append (default): ${append:template_var}            # Output: Class_sub
Append (manual): ${append('_sup'):template_var}     # Output: Class_sup
``` 

This has, however, two drawbacks:
1. We can so far only pass strings as arguments, since the arguments are read as string and get 
passed on unconverted.
2. We can pass an arbitrary number of arguments, which will result in a `TypeError` if the 
function does not accept that many arguments.  
*(This can be desired for functions that actually accept arbitrary number of arguments, 
note however that all arguments will be passed as string)* 

The workaround is to use the third argument **args** of the `add_function_hook()` method, which 
allows to define conversion operators: 

```python
# a hook that multiplies the input text 
def hook_multiply_text(input_string, count=2):
    return count * input_string
# register with the optional argument, which must be converted to integer
SmartTemplate.add_function_hook('multiply_with_arg', hook_multiply_text, [int])
```

When found, this hook will accept zero or one argument, and if one argument is found, it will be 
converted by the passed conversion function, i.e. `int(argument)`. Any further arguments found in the
template code will be dismissed and a warning (`smart_template.exceptions.TypeWarning`) will be 
issued.
Note that if fewer arguments are found in the template than specified in the **args** argument,
the additional conversion operations will be ignored to allow for optional arguments. 

*Note:* All arguments are positional, it is not possible to pass keyword/value pairs to 
the hook functions.

*Note:* If for some reason you want to remove a hook later on, you can always call the 
`remove_function_hook()` method with the name of the hook as parameter.

### Allowed names for hooks 

The default accepted naming scheme of a hook is described by the regular expression 
`[_a-z][_a-z0-9]*`, i.e. it must start with a letter or an underscore, followed by further 
underscores and/or alphanumeric characters.  
If further characters are required, see the subclassing section (Advanced) below.

### Hook Arguments

Hook arguments have a few more limitations on their handling.

 * **Whitespace**: Whitespace around arguments will not be trimmed (after all, it could be a desired
                   part of a string). Thus, if you do not want whitespace to appear in the result,
                   put all hook arguments immediately next to the comma.

    Assume we have the following function and hook defined:
    ```python
    def append(input_string, append_string_1, append_string_2, count_string_2):
       return input_string + append_string_1 + count_string_2 * append_string_2 
    SmartTemplate.add_function_hook('append', append, [str, str, int])
    ```
    Depending on the template we can get different results:
    ```
    # template_var = 'Class'
    # normal
    ${append(_sub,_sup,1):template_var}     # Output: Class_sub_sup
    # whitespace around a string argument
    ${append(_sub, _sup,1):template_var}    # Output: Class_sub _sup
    # whitespace around a numeric argument
    ${append(_sub,_sup, 2):template_var}    # Output: Class_sub_sup_sup
    ```
    For the numeric argument the whitespace does not matter, since it is removed by `int`. In the 
    string, however, this whitespace is kept and will appear in the output.
 * **Parenthesis**: Due to the nature of the parsing, ***no*** closing parenthesis ')' are allowed 
                    inside the argument list, as this would end the list and lead to invalid elements
                    afterwards. If you really need this character, you will have to find another way,
                    e.g. write some very specific text and a custom replace hook.   

### Predefined-Hooks

A number of hooks that can be used for advanced text substitution have been predefined. 
These can be loaded from the package

```python
from smart_template.hooks.formatting import lower, upper, capitalise
from smart_template.hooks.code import indent, trim, wrap
from smart_template.hooks.edit import replace
```

The list of pre-defined hooks includes the following functions
 * `lower`, `upper`  
   Convert the string to lower/upper-case. Refer to `string.lower()` or `string.upper()`
 * `capitalise`  
   Make the first letter uppercase, leave the remaining string
 * `indent(<indentation>)`
   Indent the string by a given number of spaces. This hook requires an integer argument with the number of spaces to indent the text.
 * `trim(<left>, <right>)`  
   Trim the *left* and/or the *right* side of the template variable.
 * `wrap(<width>)`  
   Wraps the given input text to a maximum *width* for each line 
 * `replace(<old>, <new>[, count])`  
   Replaces the *old* text with the *new* one. If *count* is given, at most *count* occurrences will be replaced in the text. Refer to `string.replace()`.
   
## Advanced 

### Logging

This class supports logging. If a logger is configured in the main script, any smart_template will also try to output logging information. By default, only `CRITICAL` errors will be logged. This can be set by the objects constructor: 

```python
import logging

logging.basicConfig(format='%(levelname)s\t| %(module)s.%(funcName)s: %(message)s')
template = SmartTemplate('${template_var}', logging_level=logging.DEBUG)
```

The logger used internally can be retrieved by the name of the module where it is used 
(`__name__`):
 
```python
logger = logging.getLogger('smart_template')
```

### Subclassing

As with `string.Template`, it is possible to subclass this class. The most relevant attributes to
overwrite are:

 * *delimiter*: The literal used to find template variables.
 * *pattern_id*: The regular expression pattern used to find template variables. Default is 
                 `(?:[_a-z][_a-z0-9]*)`. If *pattern_brace_id* is `None`, this will also be 
                 applied there.
 * *pattern_brace_id*: The pattern used to find braced template variables. Defaults to `None`, i.e.
                       uses *pattern_id*
 * *pattern_function_id*: The pattern used to detect hooks and their arguments. It contains itself
                          named capture groups, which are used when evaluating the hook and its
                          arguments. Defaults to:
    ```
    (?P<hook>[_a-z][_a-z0-9]*)              # name of the function hook
    (?:\(                                   # start list of arguments
        (?P<arguments>[^\)]+)               # allow  anything that is not a closing bracket
    \))?
    ``` 
  * *re_flags*: The flags applied to the regular expression.
  
You can, of course, also overwrite anything else. But you will have to figure out how to do that 
on your own, it is not that difficult. 

### Exceptions

This class defines two user defined exceptions in `smart_template.exceptions`

 * `TypeWarning`: Is used instead of type error, to issue a warning only
 * `KeyExistsError`: Is an exception raised when a dictionary entry should be overwritten
   
## Differences to `string.Template`

Compared to `string.Template` a few things behave differently:

* The **attributes** are named differently. This is basically since I did not like the old naming 
  scheme, and since I decided against subclassing anyway, there is no need to keep it.
* As of now, no `safe_substitute()` method is implemented. This means erroneous templates can 
  currently ***not*** be parsed at all.
   
## FAQ

### Why not derive from string.Template

I tried. But that class cannot be easily overwritten, and I ended up overwriting nearly any class
method, and partially event he class attributes. At that point, it just didn't seem reasonable any 
more, so I decided on rewriting the whole thing, based on the `string.Template` implementation in
Python 3.7. 

### Why do I have to define all hooks?

This is a safety measure. It would be possible to allow the usage of any builtin, or even `eval()` 
arbitrary hooks, however this would be a major security risk. By only using previously, manually 
registered hooks, the coder knows exactly which functions can be executed and has full control
on the template generation process.  

[sd]: https://tseverin.gitlab.io/smart_template
