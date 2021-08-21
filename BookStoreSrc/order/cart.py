class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart

    def add(self, book, book_qty):
        """ adding and updating the users cart session data """
        book_id = book.id
        if book_id not in self.cart:
            self.cart[book_id] = {'price': book.unit_price, 'qty': int(book_qty)}
        self.session.modified = True

    def __len__(self):
        """ get the cart data and count the quantity of items """
        return sum(item['qty'] for item in self.cart.values())
