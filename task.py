class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value) -> None:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def contains(self, value) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: Node, value) -> bool:
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def find_min(self):
        if self.root is None:
            raise ValueError("Дерево порожнє")
        return self._get_min_node(self.root).value

    def _get_min_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        if self.root is None:
            raise ValueError("Дерево порожнє")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def count(self) -> int:
        return self._count_nodes(self.root)

    def _count_nodes(self, node: Node) -> int:
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def delete(self, value) -> None:
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current: Node, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            successor = self._get_min_node(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def to_list(self) -> list:
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node: Node, result: list) -> None:
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)


if __name__ == "__main__":
    print("=== Практична робота №8: Бінарне дерево пошуку (BST) ===")
    bst = BinarySearchTree()

    sample_values = [3, 1, 9, 1, 7, 10, 6, 8]
    print(f"\n--- 1. Додавання елементів: {sample_values} ---")
    for val in sample_values:
        bst.insert(val)

    print(f"Всі елементи (in-order): {bst.to_list()}")
    print(f"Загальна кількість елементів: {bst.count()}")

    print(f"Найменший елемент: {bst.find_min()}")
    print(f"Найбільший елемент: {bst.find_max()}")

    print("\n--- 2. Перевірка пошуку ---")
    print(f"Чи є елемент 7 у дереві: {bst.contains(7)}")
    print(f"Чи є елемент 42 у дереві: {bst.contains(42)}")

    print("\n--- 3. Видалення елементів ---")
    print("Видаляємо значення 3 (має 2 нащадки, заміна на найлівіший з правого піддерева — 6)...")
    bst.delete(3)
    print(f"Елементи після видалення 3: {bst.to_list()}")
    print(f"Нова кількість елементів: {bst.count()}")

    print("\nВидаляємо значення 6...")
    bst.delete(6)
    print(f"Елементи після видалення 6: {bst.to_list()}")