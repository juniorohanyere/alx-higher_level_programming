#include <stdio.h>

#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 *
 * @list: a list
 *
 * Return: return 0 if there is no cycle
 *	   return 1 if there is cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *list1 = list;
	listint_t *list2 = list;

	if (!list)
		return (0);

	while (1)
	{
		if (list1->next != NULL && list1->next->next != NULL)
		{
			list1 = list1->next->next;
			list2 = list2->next;

			if (list1 == list2)
				return (1);
		}
		else
			return (0);
	}

}
