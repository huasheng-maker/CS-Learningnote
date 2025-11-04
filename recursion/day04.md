# CS61A --自学随笔 -day 04

------

## 递归 Recursion
- ***编写一个递归函数时，最好把函数分为基本情况和递归情况***
- ***递归的信仰之跃（Leap of Faith）***
  * 我们**相信**move_stack(n-1,start,temp)能正确地将n-1个盘子从start移动到temp
  * 然后我们移动最大的盘子（这是明确的）
  * 再**相信**move_stack(n-1,temp,end)能正确地将n-1个盘子移回来

- 数学归纳法的思想
  * **基础**：n=1时，我们知道怎么移动
  * **归纳**：如果n=k-1时能正确移动，那么n=k也能正确移动
  * **结论**：这对任意n的取值都成立

- 分治思想
  * 定义最简单的情况（n=1）
  * 定义如何将大问题分解为小问题
  * **相信递归调用能正确地解决子问题**
## Luhn Algorithm
- 检验银行卡号、信用卡号是否输入正确

## 树递归 Tree Recursion
- Tree-shaped processes arise whenever executing the body of a recursive function makes more than one call to that function.
