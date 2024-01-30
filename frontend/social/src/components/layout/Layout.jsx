import { Button, Container, Divider, Stack, Typography } from "@mui/material";
import { Link, Outlet } from "react-router-dom";

export default function Layout() {
    return <>
        <Container maxWidth="sm">
            <Stack direction={"row"}>
                <Typography variant="h4">Socialize</Typography>
                <Stack direction={"row"} 
                    marginLeft={"auto"} 
                    alignItems={"center"}
                    divider={<Divider orientation="vertical" flexItem />}>
                    <Button component={Link} to="/">Home</Button>
                    <Button component={Link} to="/signin">Sign In</Button>
                    <Button component={Link} to="/signup">Sign Up</Button>
                </Stack>
            </Stack>

            <Outlet />

        </Container>
    </>
}