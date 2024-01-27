import { Button, Card, CardContent, Divider, FormGroup, Stack, TextField, Typography } from "@mui/material";
import useApi from "../hooks/api-client";
import { useNavigate } from "react-router-dom";

export default function SignIn() {

    const apiClient = useApi()
    const navigate = useNavigate()

    async function signin(evt){
        evt.preventDefault();
        const form = evt.target;
        const formData = new FormData(form);

        const formJson={}
        formData.forEach((v, k)=>formJson[k] = v)

        const resp = await apiClient.post("/auth/signin", formJson);
        if(resp.data){
            sessionStorage.setItem("token", resp.data.token);
            if(!localStorage.getItem('returning')){
                navigate("/profile")
            }
            else{
                navigate("/posts")
            }
        }
    }

    return <Stack minHeight={"80dvh"} justifyContent={"center"}>
        <Card>
            <CardContent>
                <form onSubmit={signin}>
                    <Stack p={5}>

                        <Typography variant="h6">Sign In</Typography>
                        <Divider sx={{ my: 2 }} />

                        <FormGroup sx={{mb:2}}>
                            <TextField type="text" name="username" size="small" label="Username" />
                        </FormGroup>

                        <FormGroup sx={{mb:2}}>
                            <TextField type="password" name="password" size="small" label="Password" />
                        </FormGroup>

                        <Button sx={{}} type="submit" variant="contained">Sign In</Button>
                    </Stack>
                </form>
            </CardContent>
        </Card>
    </Stack>
}