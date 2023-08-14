#include <stdio.h>

#include "lists.h"

/**
 * is_palindrome - function to check if a singly linked list is palindrome
 *
 * @head: tge first node
 *
 * Description: an empty list is a palindrome
 *
 * Return: return 0 if it is not palindrome
 *	   return 1 if palindrome
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (validate(head, *head));
}

/**
 * validate - function to validate if a list is palindrome
 *
 * @first: the first node
 * @last: the last node
 *
 * Return: return 0 if it is not palindrom
 *	   return 1 if palindrome
*/

int validate(listint_t **first, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (validate(first, last->next) && (*first)->n == last->n)
	{
		*first = (*first)->next;
		return (1);
	}
	return (0);
}
