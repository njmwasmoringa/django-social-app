import { Button, Card, CardActions, CardContent, CardMedia, Divider, FormGroup, Paper, TextField, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import useApi from "../hooks/api-client";

export default function Post() {

    const [media, setMedia] = useState();
    const [posts, setPosts] = useState();
    const apiClient = useApi();

    useEffect(getPosts, []);

    function getPosts(){
        apiClient.get("/posts").then(response=>{
            if(response.data){
                setPosts(response.data);
            }
        })
    }

    function onSelectFile(evt){
        const selecteFile = evt.target.files[0];
        const fileReader = new FileReader();

        fileReader.onload = (e)=>setMedia(e.target.result);

        fileReader.readAsDataURL(selecteFile);

    }

    async function doPost(evt){
        evt.preventDefault();
        const form = evt.target;
        const fd = new FormData(form);
        const response = await apiClient.post('/posts/', fd, {
            headers:{
                "Content-Type": "multipart/form-data"
            }
        });

        setMedia(undefined);
        form.reset();
        getPosts();
    }

    return (<>
        <Paper sx={{ p: 3 }}>
            <Typography>Post something</Typography>
            <Divider />
            <form onSubmit={doPost}>
                <FormGroup>

                    <TextField multiple name="message" 
                        placeholder="Type what is in your mind"
                        maxRows={4}></TextField>
                    <div>
                        { media && <img src={media} width={"100%"} /> }
                    </div>
                    <input type="file" name="media" onChange={onSelectFile} />
                </FormGroup>

                <br/>
                <Button variant="contained" type="submit">Post</Button>
            </form>
        </Paper>

        { posts && posts.map(post=><Card sx={{ maxWidth: "100%", mt:4 }} key={post.id}>
                <CardMedia
                  sx={{ height: 140 }}
                  image={post.media}
                  title="green iguana"
                />
                <CardContent>
                  <Typography variant="body2" color="text.secondary">
                    {post.message}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small">Share</Button>
                  <Button size="small">Learn More</Button>
                </CardActions>
              </Card>)
        }
    </>);
}