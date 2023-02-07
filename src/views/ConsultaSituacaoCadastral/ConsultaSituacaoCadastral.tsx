import { Box, Button, FormLabel, Text, Image, Spinner, Modal, ModalOverlay, ModalContent, ModalCloseButton, ModalBody, useDisclosure } from '@chakra-ui/react'
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import classes from "./ConsultaCpf.module.css";
import image from "../../asset/ConsultaCPF.png"


function ConsultaSituacaoCadastral() {
    const { handleSubmit, register, setValue } = useForm<FormCpf>();
    const [img, setImg] = useState(false)
    const [spinner, setSpinner] = useState(false);
    const [a, setA] = useState<any>()
    const [loading, setLoading] = useState(false);
    const { isOpen, onOpen, onClose } = useDisclosure()


    type FormCpf = {
        cpf: string;
        nome: string;
    }


    async function onSubmit(register: FormCpf) {
        const cpf = register.cpf.replace(/\s/g, '')
        console.log(cpf)
        setImg(false)
        setSpinner(true)
        setLoading(true)
        fetch(`http://localhost:5000/buscarcpf/${cpf}`)
            .then(res => res.json())
            .then(data => {
                console.log(data.caminho)
                setValue("cpf", "")
                setImg(true)
                setSpinner(false)
                setA(register.cpf)
                setLoading(false)

            })
            .catch(function (error) {
                console.log(error)
                setValue("cpf", "")
                setSpinner(false)
                setImg(false)
                setLoading(false)

            })
    }



    return (
        <><Box>
            <Box className={classes.boxForm}>
                <Text
                    color={"#271B67"}
                    fontSize="4xl">
                    Consulta Situação Cadastral
                </Text>
                <form
                    className={classes.formCpf}
                    onSubmit={handleSubmit(onSubmit)}>

                    <Box className={classes.boxInput}>
                        <FormLabel>
                            CPF
                        </FormLabel>
                        <input
                            {...register("cpf")}
                            className={classes.formInput} />

                    </Box>
                    <Box className={classes.boxButtonForm}>

                        {loading
                            ?
                            <Button
                                isLoading
                                bgColor={"#271B67"}
                                type='submit'
                                className={classes.buttonForm}
                            >
                                Pesquisar
                            </Button> :
                            < Button
                                bgColor={"#271B67"}
                                type='submit'
                                className={classes.buttonForm}
                            >
                                Pesquisar
                            </Button>}
                    </Box>


                </form>
                <Box
                    width={"100%"}
                    display={"flex"}
                    justifyContent={"center"}
                    marginTop={"50px"}
                    marginBottom={"50px"}>
                    {spinner ?
                        <Box
                            display={"flex"}
                            flexDir={"column"}
                            alignItems={"center"}
                            margin={"100px"}
                        >
                            <Spinner />
                        </Box> :

                        <div />}
                    {img &&
                        <Image
                            width={"60%"}
                            src={image}
                            borderRadius={"10px"}
                            onClick={onOpen} />}
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
                                    src={image}
                                    borderRadius={"10px"} />
                            </ModalBody>
                        </ModalContent>
                    </Modal>
                </Box>
            </Box>
        </Box>
        </>
    )
}

export default ConsultaSituacaoCadastral
