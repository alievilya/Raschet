<template>
    <li>
<!--        2-->
<!--        <span>-->
<!--        <input type="checkbox">-->
<!--            <strong></strong>-->
<!--           3-->
<!--        </span>-->
<!--        211-->
<!--        <button>-->
<!--        &times;-->
<!--        </button>-->
        {{ each.title }}

    </li>

</template>

<script>
export default {
    props:{
        each:{
            type: Object,
            required: true
        }
    }
}

</script>
