#include <stdio.h>
#include <stdlib.h>
#include <python.h>

/**
 * print_python_list_info - prints info about python list
 * @p: pointer to python list
 *
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;
	Py_ssize_t len;
	Py_ssize_t index;

	len = PyList_Size(p);

	printf("Python list: [");
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("%s", PyUnicode_AsUTF8(item));
		if (i != len - 1)
			printf(", ");
	}
	printf("]\n");

	size = PyList_GET_SIZE(p);
	printf("size: %lu\n", (unsigned long)size);

	index = PyList_GET_SIZE(p);
	printf("capacity: %lu\n", (unsigned long)index);

	printf("length: %lu\n", (unsigned long)len);

}
