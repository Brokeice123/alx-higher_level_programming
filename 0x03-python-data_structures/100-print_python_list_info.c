#include <Python.h>

/**
 * print_python_list_info - prints info about python list
 * @p: pointer to python list
 */

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Object is not a list.\n");
		return;
	}

	int size = PyList_Size(p);

	printf("Size of the list: %d\n", size);
	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Type of element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

