# _idea
This is the start of it all: the _idea

This is the basis of many cerebral capabilities -- including language.

This library may be imported or installed via `pip install .` from this top-level directory.

# Theory
The context-free grammar responsible for these mechanisms is:
```
<idea>: <intent> ( <entity> ( <relationship> <entity> )? )* <idea>*
<intent>: <understand> | <be_understood>
<understand>: inquire | imitate
<be_understood>: declare | originate
<entity>: point | person/thing | concept | anonymous
```

Notice that entity has an anonymous class that allows unspecified objects, such as when using intransitive verbs according to the English language or when describing an entity's relationship to the world around it (e.g., What is the maximum speed of a Boeing 747?)

In the above example, "What is the maximum speed of a Boeing 747?", the parsing would take place as follows:
```
<idea>
  |
 \|/
  V
inquire calculate relationship anonymous speed 'boeing 747'

```
