var on_search = document.getElementById('search');
var form = document.querySelector('#form')
var search = on_search.value;
on_search.selectionEnd = search.length
on_search.focus()

on_search.addEventListener('input', function(event){

    setTimeout(function(){
    form.submit()}, 200)

})
//
//function edit(name, qnt, stock){
//        p_selected.value = name
//        p_qnt.value = qnt
//        p_qnt.disabled = false
//        add_p.disabled = false
//        p_qnt.max = stock
//
//        console.log(stock)
//    };
//
//var p_name = document.getElementById('p_name');
//    var p_qnt = document.getElementById('qnt');
//    var add_p = document.getElementById('add');
//    var remove_p = document.getElementById('remove');
//    var p_selected = document.getElementById('selected_p');
//    var p_price = document.getElementById('p_price');
//
//    function selected(name, price, stock){
//        p_qnt.value = ''
//        add_p.disabled = true
//
//        p_selected.value = name
//        p_qnt.disabled = false
//
//        p_qnt.max = stock
//
//        console.log(stock)
//
//    };
//
//    function edit(name, qnt, stock){
//        p_selected.value = name
//        p_qnt.value = qnt
//        p_qnt.disabled = false
//        add_p.disabled = false
//        p_qnt.max = stock
//
//        console.log(stock)
//    };
//
//    p_qnt.addEventListener("input", function(event){
//        if ((p_qnt.value == 0) || (p_qnt.value.includes('.'))){
//            add_p.disabled = true
//        } else{
//            add_p.disabled = false
//
//        }
//
//    });
//
//    p_qnt.addEventListener("input", function(event){
//        if (((parseInt(p_qnt.value)) > this.max) || (parseInt(p_qnt.value) < 0)) {
//        add_p.disabled = true
//      }
//    });
//
//
//    function delete_p(name){
//
//        $.ajax({
//          type: 'POST',
//          url: 'pos/p_selected_delete',
//          data: {
//            'p_name': name,
//            'csrfmiddlewaretoken': '{{ csrf_token }}'
//          },
//          success: function(data) {
//            // Response succeeds
//            console.log("deleted");
//            updateTable(data.products);
//          }
//        });
//    };
//
//    add_p.addEventListener("click", function(event){
//        console.log(p_qnt.value);
//        console.log(p_selected.value);
//
//        $.ajax({
//          type: 'POST',
//          url: 'pos/p_selected',
//          data: {
//            'p_name': p_selected.value,
//            'p_qnt': p_qnt.value,
//            'csrfmiddlewaretoken': '{{ csrf_token }}'
//          },
//          success: function(data) {
//            // Response succeeds
//            console.log("sent");
//            updateTable(data.products);
//          }
//        });
//
//        p_qnt.value = '';
//        p_selected.value = '';
//
//    })
//
//function updateTable(products) {
//      // clear the existing rows from the table
//      $('.product-table tbody').empty();
//
//      // loop through the products and create a new row for each product
//      products.forEach(product => {
//        const row = $('<tr>');
//
//        // create cells for each piece of data and add them to the row
//
//        const qntCell = $('<td>').text(product.qnt);
//        row.append(qntCell);
//
//        const nameCell = $('<td>').text(product.name);
//        row.append(nameCell);
//
//        const priceCell = $('<td>').text(product.price);
//        row.append(priceCell);
//
//        const edit_sp = $('<td><button onclick="edit(product.name, product.qnt, product.stock)" type="button" class="btn btn-primary">EDIT</button></td>')
//        row.append(edit);
//
//        const remove_sp = $('<td><button id="remove" type="button" onclick="delete_p(product.name)" class="btn btn-primary">REMOVE</button></td>')
//        row.append(remove);
//
//        // add the row to the table
//        $('.selected-product-table tbody').append(row);
//      });
//    }