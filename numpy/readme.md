# numPy
- it's basicly a package for an N-dimansional arrays.
--- 
## few function:
* identity : is making the main diagonal all ones 
```python
arr = np.identity((5))
        [[1,0,0,0,0]
        [0,1,0,0,0]
        [0,0,1,0,0]
        [0,0,0,1,0]
        [0,0,0,0,1]]
```
* full : is making the full array as you want 
 ```python
arr  = np.full((2,3),4)
print(arr)
        [[4 4 4]
        [4 4 4]]
```
* full_like : is making the array look like a prevouse array you made in the file 
``` python 
ar = np.full_like(arr,1)
print(ar)
    [[1 1 1]
    [1 1 1]]
```
* randem.rand : is making the array full with randem dicimal numbers
```python
arr = np.random.rand(2,3)
print(arr)
    [[0.35027643 0.36766482 0.48194458]
 [0.78369274 0.07581075 0.9240189 ]]
```
* repeat : it's a function for repeating an array few times 
```python
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)
        [[1 2 3]
        [1 2 3]
        [1 2 3]]
```
* copy : is making a copy of an array 
```python
acopy = arr.copy()
print(acopy)
        [[1 2 3]]
```