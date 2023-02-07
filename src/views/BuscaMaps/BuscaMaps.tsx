import { Box, Button, FormLabel, Grid, GridItem, Text, Spinner, useToast, Image, ModalContent, ModalBody, Modal, ModalCloseButton, ModalOverlay, useDisclosure } from '@chakra-ui/react';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import classes from "./BuscaMaps.module.css";
import imagem from "../../asset/ImagemFrontal.png"

function BuscaMaps() {
    const [divImg, setDivImg] = useState(false)
    const [loading, setLoading] = useState(false);
    const [spinner, setSpinner] = useState(false);
    const { register, handleSubmit, setValue, setFocus, formState: { errors } } = useForm<FormCep>();
    const toast = useToast()
    const { isOpen, onOpen, onClose } = useDisclosure()



    type FormCep = {
        cpf: string;
        cep: string;
        logradouro: string;
        bairro: string;
        cidade: string;
        estado: string;
        numero: string;
    }


    const checkCep = (e: any) => {
        const cep = e.target.value
        console.log(cep)
        fetch(`https://viacep.com.br/ws/${cep}/json`)
            .then(res => res.json()).then(data => {
                console.log(data)
                setValue('logradouro', data.logradouro);
                setValue('bairro', data.bairro);
                setValue('cidade', data.localidade);
                setValue('estado', data.uf);
                setFocus('numero');
            })

    }


    async function onSubmit(register: FormCep) {
        setSpinner(true)
        setDivImg(false)
        setLoading(true);
        fetch(`http://localhost:5000/buscarcep/${register.cep}/${register.numero}`)
            .then(res => res.json())
            .then(data => {
                console.log(data)
                setSpinner(false)
                setLoading(false)
                setDivImg(true)
                setValue("cep", "");
                setValue("logradouro", "");
                setValue("bairro", "");
                setValue('bairro', "");
                setValue('cidade', "");
                setValue('estado', "");
                setValue('numero', "");


            })

            .catch(function (error) {
                console.log(error)
                setSpinner(false)
                setLoading(false)
                setValue("cep", "");
                setValue("logradouro", "");
                setValue("bairro", "");
                setValue('bairro', "");
                setValue('cidade', "");
                setValue('estado', "");
                setValue('numero', "");
                {
                    toast({
                        title: 'Endereço não encontrado.',
                        status: 'error',
                        duration: 3000,
                        isClosable: true,
                        position: "top-right"
                    })
                }
            })
    }


    return (
        <>
            <Box>
                <Grid
                    className={classes.gridForm}
                    margin={"40px"}
                >
                    <GridItem>
                        <Text
                            color={"#271B67"}
                            fontSize="4xl">
                            Busca de Endereço
                        </Text>
                    </GridItem>

                    <form onSubmit={handleSubmit(onSubmit)}>


                        <Grid
                            className={classes.gridForm}
                            templateColumns={"repeat(4, 1fr)"}
                            gap={8}
                        >

                            <GridItem>
                                <FormLabel>
                                    CEP
                                </FormLabel>
                                <input
                                    {...register("cep", {
                                        required: 'Campo obrigatório'
                                    })}
                                    className={classes.formInput}
                                    onBlur={checkCep} />
                                <Box color={"red"} fontSize={"15px"} textAlign={"center"}>{errors.numero?.message}</Box>
                            </GridItem>

                            <GridItem
                                colSpan={2}>
                                <FormLabel>
                                    Logradouro
                                </FormLabel>
                                <input
                                    {...register("logradouro")}
                                    className={classes.formInput}
                                    type="text"
                                    name="logradouro" />
                            </GridItem>
                            <GridItem>
                                <FormLabel>Número</FormLabel>
                                <input
                                    {...register("numero", {
                                        required: 'Campo obrigatório'
                                    })}
                                    className={classes.formInput}
                                    type="number"
                                    name="numero" />
                                <Box color={"red"} fontSize={"15px"} textAlign={"center"}>{errors.numero?.message}</Box>
                            </GridItem>

                        </Grid >

                        <Grid
                            className={classes.gridForm}
                            templateColumns="repeat(3, 1fr)"
                            gap={8}
                        >

                            <GridItem>
                                <FormLabel>Bairro</FormLabel>
                                <input
                                    {...register("bairro")}
                                    className={classes.formInput}
                                    type="text"
                                    name="bairro" />
                            </GridItem>

                            <GridItem>
                                <FormLabel>Cidade</FormLabel>
                                <input
                                    {...register("cidade")}
                                    className={classes.formInput}
                                    type="text"
                                    name="cidade" />
                            </GridItem>

                            <GridItem>
                                <FormLabel>Estado</FormLabel>
                                <input

                                    {...register("estado")}
                                    className={classes.formInput}
                                    type="text"
                                    name="estado" />
                            </GridItem>

                        </Grid>

                        <Box className={classes.boxButtonForm}>
                            {loading
                                ?
                                <Button
                                    isLoading
                                    bgColor={"#271B67"}
                                    type='submit'
                                    className={classes.buttonForm}
                                >
                                    Buscar endereço
                                </Button> :
                                < Button
                                    bgColor={"#271B67"}
                                    type='submit'
                                    className={classes.buttonForm}
                                >
                                    Buscar endereço
                                </Button>}
                        </Box>
                    </form>
                </Grid>
                <Box
                    width={"100%"}
                    display={"flex"}
                    justifyContent={"center"}
                    marginTop={"50px"}
                    marginBottom={"50px"}>

                    {spinner && <Spinner /> }
                    
                    {divImg &&
                        <Box width={"60%"}>
                            <Image onClick={onOpen} src={imagem} borderRadius={"10px"}></Image>
                        </Box> }
                </Box>
                <Box>

                    <Modal size={"xxl"} isOpen={isOpen} onClose={onClose}>
                        <ModalOverlay
                            bg='blackAlpha.300'
                            backdropFilter='blur(10px) hue-rotate(90deg)' />
                        <ModalContent>
                            <ModalCloseButton />
                            <ModalBody
                                display={"flex"}
                                justifyContent={"center"}
                            >
                                <Image
                                    width={"70%"}
                                    src={imagem}
                                    borderRadius={"10px"} />
                            </ModalBody>
                        </ModalContent>
                    </Modal>
                </Box>
            </Box>
        </>
    )
}

export default BuscaMaps