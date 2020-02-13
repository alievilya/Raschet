

var lines = new Vue({
    delimiters: ['[[', ']]'],
    el: '#lines',
    data: {
        selected: '',
        options: [
            { text: 'Р-409, З-419П1, З-419МП', value: '6' },
            { text: 'З-416ГМ', value: '3' },
            { text: 'Р-431АМ', value: '4' },
            { text: 'Р-423АМ', value: '4' },
        ],
    },
});


var canals = new Vue({
    delimiters: ['[[', ']]'],
    el: '#canals',
    data: {
        message: '',
        selected: ' ',
        options: [
            { text: 'ТГ', value: '2' },
            { text: 'ТЧ', value: '2' },
            { text: 'Цифровой поток (канал)', value: '1.4' },
        ],
    },
});

var number = new Vue({
    delimiters: ['[[', ']]'],
    el: '#number',
    data: {
        message: '',
        number_val: '',
    },
});

// second page - Page2.html

var mest = new Vue({
    delimiters: ['[[', ']]'],
    el: '#mest',
    data: {
        message: '',
        selected: ' ',
    },
});

var temp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#temp',
    data: {
        message: '',
        temp_val: '',
    },
});

var snow = new Vue({
    delimiters: ['[[', ']]'],
    el: '#snow',
    data: {
        message: '',
        snow_val: '',
    },
});

var wind = new Vue({
    delimiters: ['[[', ']]'],
    el: '#wind',
    data: {
        message: '',
        wind_val: '',
    },
});