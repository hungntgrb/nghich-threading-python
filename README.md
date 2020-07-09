# Play a bit with Python Threading

### WITHOUT threading

```
Start afunc(3)...
    End afunc(3)!
Start afunc(2)...
    End afunc(2)!
Start afunc(1)...
    End afunc(1)!
```

> Took **6.001063** secs.

---

### WITH threading

```
Start afunc(3)...
Start afunc(2)...
Start afunc(1)...
    End afunc(1)!
    End afunc(2)!
    End afunc(3)!
```

> Took **3.012069** secs.

---

```python
def afunc(i):
    """Simulate a function runs in i seconds."""
    print(f'Start afunc({i})...')
    time.sleep(i)
    print(f'\tEnd afunc({i})!')
```
