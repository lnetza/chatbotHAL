$(document).ready(function () {
    $('#encuesta').DataTable({

        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: 'Reporte encuestas'
            }

        ],
    });
});