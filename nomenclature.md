# All code in teeworlds should match this code guidelines.

## Brackets and Such

Hardtabs, tabsize 4.

Use Allman style brackets like this:

```
if(MyInt != 5)
{
	while(MyInt)
	{
		MyFunction(&MyInt);
	}
}
ContinueMyStuff();
```

## Comments

Use `//` style comments for most things. Larger blocks of comments can use `/* */` style but shouldn't be used inside function bodies.

## Identifiers

Use [CamelCase](http://en.wikipedia.org/wiki/CamelCase) with upper case on the first letter as well.

## Variable Prefixes

`m_`

Class member

`g_`

Global variable

`s_`

Static variable

`_p`

Pointer

`_a`

Fixed array

Combine them appropriately.

## Class Prefixes

`C`

Class, CMyClass, This goes for structures as well.

`I`

Interface, IMyClass

## Null pointers

Use `0` or `0x0` instead of `NULL`. Because Teeworlds uses C++03, `nullptr` does not work either.

## Passing Variables

Pass by value for smaller things, const reference for larger objects. By pointer if the function needs to modify the object. Don't cast values as just a reference. If the function needs to modify it, use a pointer to show it as well.

```
void MyFunction(int MyVar);
void MyFunction(const CMyClass &MyVar);
void MyFunction(int *pMyVar);

void MyFunction(int &pMyVar); // Never do this!
```

## Examples

```
class IMyInterface
{
public:
	virtual void MyFunction(int InputVar) = 0;
};

class CMyImplementation : public IMyInterface
{
	static int ms_StaticCounter;
	int m_aSomeData[16];
public:
	void *m_pMyData;

	virtual void MyFunction(int InputVar)
	{
		// ...
	}
};
 ```
