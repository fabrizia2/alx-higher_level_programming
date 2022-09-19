#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *@list: singly list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *link = link->next;
	listint_t *last = last->next->next;

	if (list == NULL || list->next == NULL)
		return (0);

	link = list->next;
	last = last->next->next;

	while (link && last && last->next)
	{
		if (link == last)
			return (1);

		link = link->next;
		last = last->next->next;
	}

	return (0);
}
