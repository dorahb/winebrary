var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var bookId = this.dataset.book
        var action = this.dataset.action
        console.log('bookId:', bookId, 'Action:', action)

        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
          updateUserCart(bookId, action)
        }

    })
}


function updateUserCart(bookId, action){
    console.log('User is logged in, sending data...')

    var url = '/update_swap/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'bookId':bookId, 'action':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
       
    })
}