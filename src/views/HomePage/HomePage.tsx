import logo from "../../asset/img/Compliance.svg"
import { Box, Image } from '@chakra-ui/react'
import classes from "./HomePage.module.css";
import 'animate.css';


function HomePage() {

  return (
    <>
      <Box className={classes.boxForm}>
        <Box className={classes.boxForm} >
          <Image
            className="animate__animated animate__slideInRight "
            src={logo}
          />
       
      </Box>
      </Box>
    </>
  )
}

export default HomePage