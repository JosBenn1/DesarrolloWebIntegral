$('.btn-aceptar').on('click', function(){
    swal({
      title: 'Da click en el boton de descarga para obtener tu orden de pago',
      confirmButtonText: '<i class="zmdi zmdi-download"></i>  Descargar',
      confirmButtonColor: '#03A9F4',
      showCancelButton: true,
      cancelButtonColor: '#F44336',
      cancelButtonText: '<i class="zmdi zmdi-close-circle"></i> Cancelar',
      html: '<div class="form-group label-floating">'+
                  '<label class="control-label" for="InputSearch">write here</label>'+
                  '<input class="form-control" id="InputSearch" type="text">'+
            '</div>'
    }).then(function () {
      swal(
        'Listo',
        ''+$('#InputSearch').val()+'',
        'success'
      )
    });
});