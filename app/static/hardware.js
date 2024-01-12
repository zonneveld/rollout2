function dummy_command()
{
    let dummydata ={
        command:"NOTHING",
        body:[null,null,1]
    }
}

function post_command()
{
    fetch("https://jsonplaceholder.typicode.com/posts", {

    method: 'post',
    body: post,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    .catch((error)=>{
        console.log(erro)
    })

}).then((response) => {

    return response.json()

}).then((res) => {

    if (res.status === 201) {

        console.log("Post successfully created!")

    }

}).catch((error) => {

    console.log(error)

})
}