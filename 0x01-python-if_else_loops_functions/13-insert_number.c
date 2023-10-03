#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a new node at the beginning of a list
 * @head: pointer to pointer of first node of list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}

	return (new);
}
