# Dictionaries


- Dictionaries are collections of key-value pairs
- 字典是键值对的集合


## Limitations  On Dictionaries

- 字典的键有俩个限制(restrictions)
  * 字典的键**不能**是一个(unhashable type)列表或者字典(or any mutable type)
  * **任意**俩个键不能是相等的；1个键可以对应多个值

------

## Dictionary Comprehension

### 字典表达式的格式 
- {(key exp):(value exp) for (name) in (iter exp) if (filter exp)}

- 一个表达式被评估为字典的评估过程
  * Add a new frame with the current frame as its parent
  * Create an empty result dictionary that is the value of the expression
  * For each element in the iterable value of (iter exp)
    - Bind (name) to that element in the new frame from step1
    - if (filter exp) evaluates to a true value, then add to the result of dictionary <br>
    an entry that pairs the value of (key exp) to the value of (value exp)
