const purchaseBtns = document.getElementsByClassName('purchase')

for (i = 0; i < purchaseBtns.length; i++) {
    purchaseBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action

        if (user == 'AnonymousUser') {
            addCookieItem(productId, action)
        } else {
            UserOrder(productId, action)
        }
    })
}

function UserOrder(productId, action) {
    console.log('User is authenticated, sending data...')

    const url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            window.location.href = "/checkout/";
        });
}


function addCookieItem(productId, action) {
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }

        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload()
}