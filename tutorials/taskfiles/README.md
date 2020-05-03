
# Tasker Tutorial

### Example of how task initialize undifined variables.
```
task _test
```

### Example of task-bash based assert system
```
task _test:fail
```

### Example of task-bash-xargs based parallel test runner
```
task _test:all
```

> OUTPUT
```
@@[test.result=fail][name=_test] at /Users/ivanne/wss/pers/metacicd.wtree/metacicd/tutorials/taskfiles
@@@[test.result=pass][name=_test] at /Users/ivanne/wss/pers/metacicd.wtree/metacicd/tutorials/taskfiles
<no value>
<no value>
@@[test.result=fail][name=_test] at /Users/ivanne/wss/pers/metacicd.wtree/metacicd/tutorials/taskfiles
all good! _test should fail
@@[test_suite.list=pass fail][test_suite.result=pass]
```
