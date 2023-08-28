#include <Python.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <bytesobject.h>
#include <floatobject.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_bytes - function that prints python bytes
 *
 * @p: pointer to PyObject p
 *
 * Return: return nothing
*/

void print_python_bytes(PyObject *p)
{
	size_t size, i;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)(p))->ob_sval, size = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", size, s);
	size >= 10 ? size = 10 : size++;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size - 1; i++)
		printf("%02hhx ", s[i]);
	printf("%02hhx\n", s[i]);
}
/**
 * print_python_float - function that prints python float
 *
 * @p: pointer to PyObject p
 *
 * Return: return nothing
*/

void print_python_float(PyObject *p)
{
	char *s;
	double n;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	n = ((PyFloatObject *)(p))->ob_fval;
	s = PyOS_double_to_string(n, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}
/**
 * print_python_list - function that prints python lists
 *
 * @p: pointer to PyObject p
 *
 * Return: return nothing
*/

void print_python_list(PyObject *p)
{
	size_t size, i, n;
	const char *s;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	n = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, n);
	for (i = 0; i < size; i++)
	{
		s = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, s);
		!strcmp(s, "bytes") ? print_python_bytes(list->ob_item[i]) : (void)s;
		!strcmp(s, "float") ? print_python_float(list->ob_item[i]) : (void)s;
	}
}
