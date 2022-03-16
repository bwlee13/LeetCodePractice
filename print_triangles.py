from collections import deque


class Solution:

    def __init__(self):
        self.ship_queue = []
        self.batch_shipment = deque([])

    def insert_ship(self, insert_and_ship_orders: [[]]):
        print(f'Input: {insert_and_ship_orders}')
        for order in insert_and_ship_orders:
            operation, code = order
            if operation == 'INSERT':
                self.batch_shipment.append(code)

            elif operation == 'SHIP':
                if len(self.batch_shipment) < 3:
                    self.ship_queue.append(['N/A'])
                else:
                    batch_of_three = []
                    counter = 3
                    while counter > 0:
                        batch_of_three.append(self.batch_shipment.popleft())
                        counter -= 1

                    self.ship_queue.append(batch_of_three)

    def get_result(self):
        return self.ship_queue


def main():
    s = Solution()
    s.insert_ship(insert_and_ship_orders=[['INSERT', 'GT23513413'], ['INSERT', 'TQC2451340'], ['SHIP', '-'],
                                          ['INSERT', 'VYP8561991'], ['SHIP', '-']])
    print(f'Result: {s.get_result()}')

    s = Solution()
    s.insert_ship(insert_and_ship_orders=[["INSERT", "UIAHSIHGFG"], ["INSERT", "RGSRTWR"], ["SHIP", "-"],
                                          ["INSERT", "EYJTRJYEYTJ"], ["INSERT", "QERGFSFDS"], ["SHIP", "-"]])
    print(f'Result: {s.get_result()}')

    s = Solution()
    s.insert_ship(insert_and_ship_orders=[["INSERT", "UIAHSIHGFG"], ["INSERT", "RGSRTWR"], ["SHIP", "-"],
                                          ["INSERT", "EYJTRJYEYTJ"], ["INSERT", "QERGFSFDS"], ["SHIP", "-"],
                                          ["INSERT", "QERGFSFDS2"], ["SHIP", "-"], ["INSERT", "QERGFSFDS3"],
                                          ["SHIP", "-"]])
    print(f'Result: {s.get_result()}')


if __name__ == '__main__':
    main()
Input: [['INSERT', 'GT23513413'], ['INSERT', 'TQC2451340'], ['SHIP', '-'], ['INSERT', 'VYP8561991'], ['SHIP', '-']]
Result: [['N/A'], ['GT23513413', 'TQC2451340', 'VYP8561991']]
Input: [['INSERT', 'UIAHSIHGFG'], ['INSERT', 'RGSRTWR'], ['SHIP', '-'], ['INSERT', 'EYJTRJYEYTJ'],
        ['INSERT', 'QERGFSFDS'], ['SHIP', '-']]
Result: [['N/A'], ['UIAHSIHGFG', 'RGSRTWR', 'EYJTRJYEYTJ']]
Input: [['INSERT', 'UIAHSIHGFG'], ['INSERT', 'RGSRTWR'], ['SHIP', '-'], ['INSERT', 'EYJTRJYEYTJ'],
        ['INSERT', 'QERGFSFDS'], ['SHIP', '-'], ['INSERT', 'QERGFSFDS2'], ['SHIP', '-'], ['INSERT', 'QERGFSFDS3'],
        ['SHIP', '-']]
Result: [['N/A'], ['UIAHSIHGFG', 'RGSRTWR', 'EYJTRJYEYTJ'], ['N/A'], ['QERGFSFDS', 'QERGFSFDS2', 'QERGFSFDS3']]