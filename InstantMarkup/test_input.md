
  前一篇介绍了“换元法”和“分部积分”两种一般的求积分的方法，这一篇主要学习对“有理式”和“简单无理式”求积分的套路。这一篇是对不定积分方法的总结，在此特地介绍一个[在线积分器](http://um.mendelu.cz/maw-html/menu.php)和[symbolab](https://www.symbolab.com/solver/partial-fractions-calculator)，对于复杂的积分式可以用它们辅助计算。  

### 一、知识点

1，四个分式模式  
&emsp;&emsp;所谓的“套路”，都是通过一系列变换，把被积函数转化为[“积分表”](https://en.wikipedia.org/wiki/Lists_of_integrals)中的函数及其组合。积分表中有四个积分式对于分式有理式非常重要，甚至被总结为四种模式（pattern）。  
1）一次单因式（对数模式） 
**$$\int \frac{A}{ax+b}dx = \frac{A}{a}ln|ax+b|+C$$**  
2）一次k重因式  
**$$\int \frac{A}{(ax+b)^{k}}dx = \frac{A}{(1-k)a}\cdot \frac{1}{(ax+b)^{k-1}}+C$$**  
&emsp;&emsp;上式运用了“凑微分”。  
3）二次单因式（反正切模式）  
**$$\int \frac{Bx+D}{px^{2}+qx+r}dx = \frac{B}{2p}\int \frac{2px+q}{px^{2}+qx+r}dx + (D-\frac{Bq}{2p})\frac{1}{p}\int \frac{dx}{(x + \frac{q}{2p})^{2}+\frac{4pr-q^{2}}{4p^{2}}} \\
= \frac{B}{2p}ln\left | px^{2}+qx+r \right |+\frac{2pD-qB}{p\sqrt{4pr-q^{2}}}arctan(\frac{2px+q}{\sqrt{4pr-q^{2}}})+C$$**  
4）二次k重因式  
**$$\int \frac{Bx+D}{(px^{2}+qx+r)^{k}}dx = \frac{B}{2p(1-k)}\cdot \frac{1}{(px^{2}+qx+r)^{k-1}}+\frac{2pD-qB}{p\sqrt{4pr-q^{2}}}\int \frac{dx}{[(x + \frac{q}{2p})^{2}+(\frac{\sqrt{4pr-q^{2}}}{2p})^{2}]^{k}}$$**  
&emsp;&emsp;上式先“凑微分”，然后换元，再分部积分，并运用递归，可以求出原函数。其中，$\int \frac{dx}{(x^{2}+ a^{2})^{n}}$，n是大于1的自然数使用分部积分可以得到它的递归公式，如下：  
**$$I_{n+1}=\frac{2n-1}{2na^{2}}I_{n}+\frac{x}{2na^{2}(x^{2}+a^{2})^{n+1}}$$**  
**$$I_{1}=\frac{1}{a}arctan(\frac{x}{a})+C$$**  
2，分式有理式  
&emsp;&emsp;**定理**：设$\frac{P_{m}(x)}{Q_{n}(x)}$是一真分式，则它可以**唯一**地分解为最简分式之和。  
例：  
$$\int \frac{x+1}{x^{2}-4x+3}dx=\int [\frac{A}{x-1}+\frac{B}{x-3}]dx$$  
&emsp;&emsp;通分，解系数方程，求出A和B。 
&emsp;&emsp;分式有理式求积分的方法又称为“部分分式积分法”（[Interation by Partial Fractions](http://tutorial.math.lamar.edu/Classes/CalcII/PartialFractions.aspx)），它是基于“部分分式分解”（[Partial Fraction decomposition](https://en.wikipedia.org/wiki/Partial_fraction_decomposition)）得来的一种求特定积分的方法。sympy提供了“**apart()**”函数用于执行“部分分式分解”操作。下面再给几个相关链接：  
&emsp;&emsp;[部分分式积分](http://math.tutorvista.com/calculus/integration-by-partial-fractions.html)  
&emsp;&emsp;[partial fraction expand in matlab](https://cn.mathworks.com/help/matlab/ref/residue.html)  
3，三角函数有理式   
&emsp;&emsp;对sin(x)和cos(x)及常数进行有限次的四则运算得到的表达式称为“**三角函数有理式**”，记作**R( sin x, cos x )**，其中 R  - Rational  
&emsp;&emsp;对于三角函数有理式$\int R[sin(x), cos(x)]dx$的积分套路如下：  
&emsp;&emsp;（根据“**三角函数万能公式**”）取$t=tan\frac{x}{2}$,则$x=2arctan(t),dx=\frac{2}{1+t^{2}}dt,sin(x)=\frac{2t}{1+t^{2}},cos(x)=\frac{1-t^{2}}{1+t^{2}}$，于是可得： 
**$$\int R[sin(x), cos(x)]dx=\int R[\frac{2t}{1+t^{2}}, \frac{1-t^{2}}{1+t^{2}}]\frac{2}{1+t^{2}}dt$$**
&emsp;&emsp;很显然，这里应用的是“**反函数换元法**”（第二类换元法）。  
4，简单无理式  
&emsp;&emsp;无理式积分的困难在于被积函数中带有开发运算，因此，一般的思路是先进行“**有理化**”。如下：  
1）$\int R(x,\sqrt[n]{ax+b})dx,\; (a\neq 0)$  
&emsp;&emsp;取$ax+b=t^{n}$，可得  
**$$\int R(x,\sqrt[n]{ax+b})dx=\int R(\frac{t^{n}-b}{a},t)\frac{nt^{n-1}}{a}dt$$**  
2）$\int R(x,\sqrt[n]{\frac{ax+b}{cx+d}})dx$  
&emsp;&emsp;取$\frac{ax+b}{cx+d}=t^{n}$，可得  
**$$\int R(x,\sqrt[n]{\frac{ax+b}{cx+d}})dx = \int R(\frac{t^{n}d-b}{a-t^{n}c}, t)\frac{n(ad-cb)t^{n-1}}{(a-ct^{n})^{2}}dx$$**  
3）$\int R(x,\sqrt{ax^{2}+bx+c})dx,\; (a\neq 0)$  
&emsp;&emsp;先凑成“平方和”或“平方差”形式，再应用三角函数“平方公式”进行变量替换。  
4，可积与求出积分  
&emsp;&emsp;在“不定积分的概念”那一节，讲到“连续函数”甚至“满足介值定理的函数”都可积（原函数存在）。但是，“可积”不代表一定能求出它的积分表达式（用初等函数表示），例如：$e^{-x^{2}},\; \frac{sin(x)}{x},\; \frac{1}{ln(x)},\; \sqrt{1-\frac{1}{2}sin^{2}(x)}$。事实上，大多数初等函数的原函数都不能表示为初等函数。  

### 二、思考题

1，是否所有的分式有理函数在实数范围内都可以化为形如$\frac{a}{x - b}$简单分式的和？  
答：否！本课程中的“[Partial Fraction decomposition](https://en.wikipedia.org/wiki/Partial_fraction_decomposition)”定理只是说可以将任意有理分式分解化为最简分式，而这里所说的最简分式包含了四个，而不只是一次单因式。比如，并不是所有的二次单因式都能化为一次单因式。  
  
2，是否可以得到“分式有理函数的不定积分都可以用初等函数表示”的结论？  
答：是！首先，所有的分式有理函数都可以化为一个多项式（整式）与一个真分式之和。然后，根据定理，所有的真分式又可以分解为四个模块（最简分式）的线性组合，而最简分式都可积，且积分后的原函数都是初等函数，那么这个命题成立。  
注：这个问题非常有意思。有了计算机之后，人们开始从繁琐的运算中解放出来了，当然这个运算也包括积分运算。但是，对于计算机来说，判断一个函数是否可积，是比按程序计算积分更大的挑战。而从这个问题出发，人们可以先判断一个函数是否可积，可积再交给计算机去执行积分运算，不可积就不要浪费时间和计算资源了。或许，这也暗合“数据标记”吧！

### 三、选择题


```python
from sympy import *
init_printing()
#Exercise 6-4-3
x = Symbol('x')
integrate(1 / (1 - x ** 2), x)
```




$$- \frac{1}{2} \log{\left (x - 1 \right )} + \frac{1}{2} \log{\left (x + 1 \right )}$$




```python
#Exercise 6-4-4
t = Symbol('t')
integrate((t+4) / (t ** 2 + 5 * t - 6), t)
```




$$\frac{5}{7} \log{\left (t - 1 \right )} + \frac{2}{7} \log{\left (t + 6 \right )}$$




```python
#Exercise 6-4-5
x = Symbol('x')
integrate((2 * x ** 2 + 2 * x + 13) / ((x - 2) * (x ** 2 + 1) ** 2), x)
```




$$- \frac{4 x - 3}{2 x^{2} + 2} + \log{\left (x - 2 \right )} - \frac{1}{2} \log{\left (x^{2} + 1 \right )} - 4 \operatorname{atan}{\left (x \right )}$$




```python
#Exercise 6-4-6
x = Symbol('x')
integrate(1 / (x ** 4 + 1), x)
```




$$- \frac{\sqrt{2}}{8} \log{\left (x^{2} - \sqrt{2} x + 1 \right )} + \frac{\sqrt{2}}{8} \log{\left (x^{2} + \sqrt{2} x + 1 \right )} + \frac{\sqrt{2}}{4} \operatorname{atan}{\left (\sqrt{2} x - 1 \right )} + \frac{\sqrt{2}}{4} \operatorname{atan}{\left (\sqrt{2} x + 1 \right )}$$



&emsp;&emsp;对于$\int \frac{1}{x^{4} + 1}dx=?$，sympy已经求出了积分，但是这个结果可以写得更简单一些。其中对数表达式可以合并，反正切表达式也可以合并。关于反正切的合并如下：  
&emsp;&emsp;根据正切函数的和差公式：$tan(\alpha \pm \beta )=\frac{tan(\alpha )\pm tan(\beta )}{1\mp tan(\alpha )tan(\beta )}$，两边取反函数，可得：  
$$arctan(a)\pm arctan(b)=\alpha \pm \beta=arctan[\frac{tan(\alpha )\pm tan(\beta )}{1\mp tan(\alpha )tan(\beta )}]=arctan\frac{a \pm b}{1 \mp ab}$$  
所以，这个积分的结果可以简写为：  
$$\int \frac{1}{1+x^{4}}dx=\frac{\sqrt{2}}{8}ln\frac{x^{2}+\sqrt{2}x+1}{x^{2}-\sqrt{2}x+1}+\frac{\sqrt{2}}{4}arctan\frac{x^{2}-1}{\sqrt{2}x}+\frac{\pi }{2}+C$$  
注意：反正切函数合并后，又用了反正切函数的“负数关系”和“倒数关系”。  
下面再来看手动计算：  
1）首先试着因式分解，很明显，不是很容易分解。那么不妨假设根据有理分式的分解定理，将它分解成4个二次k重因式的组合。  
2）列方程组解出各系数。  
3）分别对各个因式积分。  


```python
#Exercise 6-5-1
x = Symbol('x')
integrate(1 / (sin(x) + 1), x)
```




$$- \frac{2}{\tan{\left (\frac{x}{2} \right )} + 1}$$




```python
#Exercise 6-5-2
x = Symbol('x')
integrate(1 / (1 - cos(x)), x)
```




$$- \frac{1}{\tan{\left (\frac{x}{2} \right )}}$$




```python
#Exercise 6-5-3
x = Symbol('x')
integrate((1+sin(x)) / (1 + cos(x)), x)
```




$$\log{\left (\tan^{2}{\left (\frac{x}{2} \right )} + 1 \right )} + \tan{\left (\frac{x}{2} \right )}$$




```python
#Exercise 6-5-4
x, a = symbols('x a')
b = Symbol('b', nonzero=True)
integrate(tan(x) / (a ** 2 * (cos(x)) ** 2 +  b ** 2 * (sin(x)) ** 2), x)
```




$$\int \frac{\tan{\left (x \right )}}{a^{2} \cos^{2}{\left (x \right )} + b^{2} \sin^{2}{\left (x \right )}}\, dx$$




```python
#Exercise 6-5-4b
x, t, a = symbols('x t a')
b = Symbol('b', nonzero=True)
expr1 = 2 * t / (1 + t ** 2)
expr2 = (1 - t ** 2) / (1 + t ** 2)
expr3 = 2 / (1 + t ** 2)
expr = simplify((expr1 / expr2) / (a ** 2 * expr2 ** 2 + b ** 2 * expr1 ** 2) * expr3)
inte = integrate(expr, t)
expr, inte
```




$$\left ( - \frac{4 t \left(t^{2} + 1\right)}{\left(t^{2} - 1\right) \left(a^{2} \left(t^{2} - 1\right)^{2} + 4 b^{2} t^{2}\right)}, \quad - \frac{1}{b^{2}} \log{\left (t^{2} - 1 \right )} + \frac{1}{2 b^{2}} \log{\left (t^{4} + 1 + \frac{t^{2}}{a^{2}} \left(- 2 a^{2} + 4 b^{2}\right) \right )}\right )$$




```python
inte.subs(t, tan(x / 2))
```




$$- \frac{1}{b^{2}} \log{\left (\tan^{2}{\left (\frac{x}{2} \right )} - 1 \right )} + \frac{1}{2 b^{2}} \log{\left (\tan^{4}{\left (\frac{x}{2} \right )} + 1 + \frac{1}{a^{2}} \left(- 2 a^{2} + 4 b^{2}\right) \tan^{2}{\left (\frac{x}{2} \right )} \right )}$$



进一步化简，将半角化简掉。  
根据三角函数半角公式：  
**$$tan(\frac{\theta }{2})=\pm \sqrt{\frac{1-cos(\theta )}{1+cos(\theta )}}=\frac{sin(\theta)}{1+cos(\theta)}=\frac{1-cos(\theta)}{sin(\theta)}$$**
代入上式，并合并对数，再化简可得：  


```python
x, t, a, b = symbols('x t a b')
expr = log((t ** 4 + 1 - 2 * t ** 2 + 4 * b ** 2 / a ** 2 * t ** 2) / (t ** 2 -1) ** 2)
expr, simplify(expr.subs(t, sqrt((1 - cos(x)) / (1 + cos(x)))))
```




$$\left ( \log{\left (\frac{1}{\left(t^{2} - 1\right)^{2}} \left(t^{4} - 2 t^{2} + 1 + \frac{4 b^{2}}{a^{2}} t^{2}\right) \right )}, \quad \log{\left (1 + \frac{b^{2}}{a^{2}} \tan^{2}{\left (x \right )} \right )}\right )$$




```python
#Exercise 6-5-5
x = symbols('x')
integrate(sin(2 * x) / ((cos(x)) ** 2 +  2 * sin(x)), x)
```




$$\int \frac{\sin{\left (2 x \right )}}{2 \sin{\left (x \right )} + \cos^{2}{\left (x \right )}}\, dx$$



很明显，这个直接积分积不出来。当然，我们也可试着用上一题的方法来换元，但是，最后的结果会很复杂，也不能像上一题一样化简。那么，我们根据它的特点来手动计算吧：  
$$\int \frac{sin(2x)}{cos^{2}(x)+2sin(x)}dx=\int \frac{sin(2x)}{1-sin^{2}(x)+2sin(x)}dx=\int \frac{2sin(x)d[sin(x)]}{1-sin^{2}(x)+2sin(x)}$$  
然后再应用换元法


```python
x, t = symbols('x t')
expr = integrate(2 * t / (1 - t ** 2 + 2 * t), t)
expr.subs(t, sin(x))
```




$$- 2 \left(- \frac{\sqrt{2}}{4} + \frac{1}{2}\right) \log{\left (\sin{\left (x \right )} - 1 + \sqrt{2} \right )} - 2 \left(\frac{\sqrt{2}}{4} + \frac{1}{2}\right) \log{\left (\sin{\left (x \right )} - \sqrt{2} - 1 \right )}$$




```python
#Exercise 6-5-6
x, t = symbols('x t')
expr = integrate(6 * t ** 4 / (t ** 5 + 1), t)
expr.subs(t, x ** (1 / 6))
```




$$\frac{6}{5} \log{\left (x^{0.833333333333333} + 1 \right )}$$




```python
#Exercise 6-5-7
x, t = symbols('x t')
expr = integrate(t * sqrt(t + 2), t)
expr
```




$$\frac{6 t^{\frac{9}{2}} \sqrt{1 + \frac{2}{t}}}{15 t^{2} + 30 t} + \frac{16 t^{\frac{7}{2}} \sqrt{1 + \frac{2}{t}}}{15 t^{2} + 30 t} - \frac{8 t^{\frac{5}{2}} \sqrt{1 + \frac{2}{t}}}{15 t^{2} + 30 t} - \frac{32 t^{\frac{3}{2}} \sqrt{1 + \frac{2}{t}}}{15 t^{2} + 30 t} + \frac{16 \sqrt{2} t^{2}}{15 t^{2} + 30 t} + \frac{32 \sqrt{2} t}{15 t^{2} + 30 t}$$




```python
#Exercise 6-5-7b
x, t = symbols('x t')
expr = integrate((t ** 2 -2) * t * 2 * t, t)
expr, expr.subs(t, sqrt(x - 2))
```




$$\left ( \frac{2 t^{5}}{5} - \frac{4 t^{3}}{3}, \quad \frac{2}{5} \left(x - 2\right)^{\frac{5}{2}} - \frac{4}{3} \left(x - 2\right)^{\frac{3}{2}}\right )$$




```python
#Exercise 6-5-8
x = symbols('x')
expr = integrate(sqrt(x ** 2 -2 * x + 1) / (x -1), x)
expr
```




$$\sqrt{x^{2} - 2 x + 1}$$




```python
#Exercise 6-5-9
x = symbols('x')
expr = integrate(sqrt(E ** x + 1), x)
expr
```




$$\int \sqrt{e^{x} + 1}\, dx$$



很明显，这个直接积分积不出来。先“有理化”换元，再积分：  


```python
#Exercise 6-5-9b
x, t = symbols('x t')
expr = integrate(2 * t ** 2 / (t ** 2 - 1), t)
expr.subs(t, sqrt(E ** x + 1))
```




$$2 \sqrt{e^{x} + 1} + \log{\left (\sqrt{e^{x} + 1} - 1 \right )} - \log{\left (\sqrt{e^{x} + 1} + 1 \right )}$$




```python
#Exercise 6-5-10
x = symbols('x')
expr = integrate(((x - 1) * (x + 1) ** 2) ** (1 / 3), x)
expr
```




$$\int \left(\left(x - 1\right) \left(x + 1\right)^{2}\right)^{0.333333333333333}\, dx$$



这一题不能直接换元，需要先变换。如下：  
$$\int \frac{dx}{\sqrt[3]{(x-1)(x+1)^{2}}}=\int \frac{dx}{(x+1)*\sqrt[3]{\frac{x-1}{x+1}}}$$


```python
#Exercise 6-5-10b
x, t = symbols('x t')
g = ((x - 1) / (x + 1)) ** (1 / 3)
eq = Eq(g, t)
solve(eq, x)
```




$$\left [ - \frac{t^{3} + 1.0}{t^{3} - 1.0}\right ]$$




```python
diff(-(t ** 3 + 1) / (t ** 3 - 1), t)
```




$$- \frac{3 t^{2} \left(- t^{3} - 1\right)}{\left(t^{3} - 1\right)^{2}} - \frac{3 t^{2}}{t^{3} - 1}$$




```python
x, t = symbols('x t')
h = diff(-(t ** 3 + 1) / (t ** 3 - 1), t)
expr = - (t ** 3 - 1) / (2 * t) * h
inte = integrate(expr, t)
inte.subs(t, ((x - 1) / (x + 1)) ** (1 / 3))
```




$$- \log{\left (\left(\frac{x - 1}{x + 1}\right)^{0.333333333333333} - 1 \right )} + \frac{1}{2} \log{\left (\left(\frac{x - 1}{x + 1}\right)^{0.333333333333333} + \left(\frac{x - 1}{x + 1}\right)^{0.666666666666667} + 1 \right )} - \sqrt{3} \operatorname{atan}{\left (\frac{2 \sqrt{3}}{3} \left(\frac{x - 1}{x + 1}\right)^{0.333333333333333} + \frac{\sqrt{3}}{3} \right )}$$




