#include <stdio.h>

#include <Python.h>

/**
 * print_python_string - funtion that prints python strings
 *
 * @p: pointer to a PyObject string
 *
 * Return: return nothing
*/

void print_python_string(PyObject *p)
{
	long int length;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
