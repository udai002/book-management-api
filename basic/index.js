const express = require('express')

const app = express()

app.post('/register/' , async (req , res)=>{
    const {username , password} = req.body;
    console.log(username)
    res.send(username)
})

app.listen(3000)
