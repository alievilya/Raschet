<template>
    <div>
        <ul>
            <item
            v-for="each in line_types"
            v-bind:each="each"
            />
        </ul>
    </div>

</template>
<script>
import item from '@/components/item'
export default{
    props:['line_types'],
    components:{
        item
        }

    }
</script>
