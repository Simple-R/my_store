var update_btn = document.getElementsByClassName('update-cart')

for (var i = 0; i< update_btn.length; i++){
  update_btn[i].addEventListener('click', function(){
    var item_id = this.dataset.item
    var action = this.dataset.action
    console.log('Product Id: ', item_id,
                'Action: ', action)
  })
}