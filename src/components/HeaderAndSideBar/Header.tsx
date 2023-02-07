import { Box, Button, Text, Image, ChakraProvider } from "@chakra-ui/react"
import classes from "./Header.module.css"
import { Link } from "react-router-dom"
import { GiHamburgerMenu } from "react-icons/gi";
import { LegacyRef } from "react";
import logo from "../../asset/img/kyc.svg"

const Header = (props: { btnRef: LegacyRef<HTMLButtonElement> | undefined, onClick: () => void }) => {

    return (
        <ChakraProvider>
            <div className={classes.header}>
                <Button
                    ref={props.btnRef}
                    variant={'unstyled'}
                    onClick={props.onClick}>
                    <GiHamburgerMenu style={{ fontSize: '30px', color: "ghostwhite" }} />
                </Button>

                <Box
                    width={"95%"}
                    display={"flex"}
                    alignItems={"center"}
                    justifyContent={"center"}>
                        <Image src={logo}></Image>
                    <Link to={"/"}>
                        <Text fontSize={"25px"} color={"white"} margin={"5px"}>
                            Compliance KYC
                        </Text>
                    </Link>

                </Box>
            </div>
        </ChakraProvider>


    )
}

export default Header