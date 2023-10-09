#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if list is palindrome, 0 otherwise
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		prev->next = NULL;

	slow = reverse_list(slow);

	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);
		slow = slow->next;
		*head = (*head)->next;
	}

	return (1);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to head of list
 * Return: pointer to head of reversed list
 *
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev;
	listint_t *current;
	listint_t *next;

	prev = NULL;
	current = head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
