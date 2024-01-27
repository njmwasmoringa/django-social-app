import { Button, Card, CardContent, Divider, FormGroup, Stack, TextField, Typography } from "@mui/material";
import { useState } from "react";
import useApi from "../hooks/api-client";
import { useNavigate } from "react-router-dom";

export default function SignUp() {

    /* const [formData, setFormData] = useState();

    function updateField(evt){
        setFormData({
            ...formData,
            [evt.target.name]: evt.target.value
        })
    } */

    const apiClient = useApi();
    const navigate = useNavigate();

    async function submitForm(evt) {
        evt.preventDefault();
        const form = evt.target;
        const formData = new FormData(form);

        const formJson = {};
        formData.forEach((v, k) => formJson[k] = v);

        const resp = await apiClient.post('/auth/signup', formJson);
        if(resp.data){
            navigate("/signin")
        }
    }

    return <Stack minHeight={"80dvh"} justifyContent={"center"}>
        <Card>
            <CardContent>
                
                <form onSubmit={submitForm}>
                    <Stack p={5}>

                        <Typography variant="h6">Sign Up</Typography>
                        <Divider sx={{ my: 2 }} />

                        <FormGroup sx={{ mb: 2 }}>
                            <TextField type="text" name="fullname" required size="small" label="Fullname" />
                        </FormGroup>

                        <FormGroup sx={{ mb: 2 }}>
                            <TextField type="text" name="username" required size="small" label="Username" />
                        </FormGroup>

                        <FormGroup sx={{ mb: 2 }}>
                            <TextField type="email" name="email" required size="small" label="Email" />
                        </FormGroup>

                        <FormGroup sx={{ mb: 2 }}>
                            <TextField type="password" name="password" required size="small" label="Password" />
                        </FormGroup>

                        <FormGroup sx={{ mb: 2 }}>
                            <TextField type="password" name="confirm_password" required size="small" label="Confirm Password" />
                        </FormGroup>

                        <Button type="submit" sx={{}} variant="contained">Sign Up</Button>
                    </Stack>
                </form>
            </CardContent>
        </Card>
    </Stack>
}