$('#table').bootstrapTable({
    columns: [
       {
        title:'全选',
        field:'select',
        //复选框
        checkbox:true,
        width:25,
        align:'center',
        valign:'middle'
            }, {
        field: 'id',
        title: 'Item ID',
        align:'center'
    }, {
        field: 'name',
        title: 'Item Name',
        align:'center'
    }, {
        field: 'price',
        title: 'Item Price',
        align:'center'
    }],
    pageNumber: 1, //初始化加载第一页，默认第一页
    pagination:true,//是否分页
    pageSize:10,//单页记录数
    search: true,
    searchOnEnterKey: true,
    searchAlign: 'right',

    data: [{
        id: 1,
        name: 'Item 1',
        price: '$1'
    }, {
        id: 2,
        name: 'Item 2',
        price: '$2'
    }]
});