#include <Python.h>

/**
 * print_python_list_info - function that prints some basic info about Python
 *			    lists
 *
 * @p: pointer to a python object
 *
 * Return: return nothing
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i, m;
	PyObject *obj;

	i = 0;
	size = PyList_Size(p);
	m = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", m);
	while (i < size)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, obj->ob_type->tp_name);
		i++;
	}
}
