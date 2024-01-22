
### Vue.js Directives
# v-cloak

# v-model


# v-if

# v-else-if

# v-else

# v-on
This directive is specific for events. We can use it for custom events that we create ourselves; or we can use it for any of the standard browser events: such as a mouse click or a press of a button on the keyboard. 
```vue.js
<button v-on:click>ShowBox</button>
```
We have created a button with a click event. Now we have to tell it what to do when a button is clicked.
```vue.js
<button v-on:click="isVisible = true">ShowBox</button>
```
Now, we tell it to change the value of the `isVisible` variable to true when the button is clicked.

Although functional, the button does not change the `isVisible` variable back to `false` when clicked again. The only way to do so is to refresh the page.

In order to fix that, we can simply  `toggle` the button. 
And in order to do that, we write the following code:
```vue.js
<button v-on:click="isVisible = !isVisible">ShowBox</button>
```

Another variation of the `v-on` directive syntax, we can write `@` instead of `v-on`:
```vue.js
<button @click="isVisible = !isVisible">ShowBox</button>
```

We can also use this directive in more complex ways. Instead of changing a variable's value, we can pass in any kind of method on our vue.js object.

In the following code, we are going to use a method that we will write called `toggleBox` instead of passing a variable and changing it's value:
```vue.js
<button @click="toggleBox">Toggle Box</button>
```