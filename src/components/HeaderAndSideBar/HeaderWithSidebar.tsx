import { useDisclosure } from "@chakra-ui/hooks";
import { useRef } from "react";
import Header from "./Header";
import Sidebar from "./Sidebar";

const HeaderWithSidebar = () => {
    const btnRef = useRef(null);
    const disclosure = useDisclosure()
    return(
        <>
            <Header btnRef={btnRef} onClick={disclosure.onOpen}/>
            <Sidebar btnRef={btnRef} disclosure={disclosure}/>
        </>
    )
}

export default HeaderWithSidebar;