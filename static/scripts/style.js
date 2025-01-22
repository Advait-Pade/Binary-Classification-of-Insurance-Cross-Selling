function setTableWidth() {
    var rows = document.querySelectorAll('table tr');
    var maxWidth = 0;

    for (var i = 1; i < rows.length; i++) {
        var cell = rows[i].querySelector('td:nth-child(1)');
        if (cell) {
            var cellWidth = cell.offsetWidth;
            if (cellWidth > maxWidth) {
                maxWidth = cellWidth;
            }
        }
    }

    console.log('Max Width:', maxWidth);

    var cells = document.querySelectorAll('table tr td:nth-child(1)');
    cells.forEach(function(cell) {
        cell.style.width = maxWidth + 'px';
    });
}

document.addEventListener('DOMContentLoaded', setTableWidth);
