import {
    Button, ButtonProps, Drawer, DrawerBody, DrawerContent, DrawerOverlay, UseDisclosureReturn, Stack, HStack, DrawerCloseButton
} from "@chakra-ui/react";
import { RefObject } from "react";
import { useNavigate } from "react-router-dom";


const ExtendedNavbarButton = (props: ButtonProps) => {
    return (
        <Button width={"100%"} variant={"ghost"} margin={0} borderRadius={0} onClick={props.onClick}>
            {props.children}
        </Button>
    );
};

const Sidebar = (props: {
    btnRef: RefObject<HTMLButtonElement> | undefined;
    disclosure: UseDisclosureReturn;
}) => {
    const { isOpen, onClose } = props.disclosure;
    const navigate = useNavigate();
    return (
        <>

            <Drawer
                isOpen={isOpen}
                placement="left"
                onClose={onClose}
                finalFocusRef={props.btnRef}
            >
                <DrawerOverlay />
                <DrawerContent padding={4}>
                    <HStack mb={2}>
                        <DrawerCloseButton />
                    </HStack>
                    <DrawerBody>
                        <Stack spacing='12px'>
                            <ExtendedNavbarButton
                                onClick={() => navigate("/buscamaps")}
                            >
                                Busca Maps
                            </ExtendedNavbarButton>

                            <ExtendedNavbarButton
                                onClick={() => navigate("/consultasituacaocadastral")}
                            >
                                Consultar Situação Cadastral
                            </ExtendedNavbarButton>
                            <ExtendedNavbarButton
                                onClick={() => navigate("/pesquisaportaltransparencia")}
                            >
                                Pesquisa Portal da Transparência
                            </ExtendedNavbarButton>
                            


                        </Stack>
                    </DrawerBody>

                </DrawerContent>
            </Drawer>
        </>
    );
};

export default Sidebar; 
