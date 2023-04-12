# epic_corrosion_project

La formation de rouille sur le fer est un processus chimique qui se produit lorsque le fer reagit avec l'oxygene et l'eau. Afin de modeliser ce processus, nous avons commencer par etablir une fonction "Rusting " qui prend en parametres les concentrations de fer ,d'ions Fe2+, d'oxygene et d'eau et deux constantes de vitesse .


Nous avons utilise les formules des reactions anodique et cathodique:

Fe -->2e- + Fe2+

2H2O+ 2e- -->H2 + 2OH-

respectivement.

Notre fonction calcule la vitesse de la reaction anodique qui convertit le fer en ions Fe2+ en presence d'eau,en utilisant l'equation suivante :

 r_anodic = k1 * iron * oxygen**(1/2) * (1 - fe2/iron)
 
 k1:une constante de vitesse.
 
 la fonction calcule ensuite la vitesse de la reaction cathodique qui convertit l'oxygene et l'eau en ions d'hydroxyde en presence d'ions Fe2+,en utilisant l'equation suivante :
 
  r_cathodic = k2 * oxygen * water**(1/2) * (1 - fe2/iron)
  
  k2: une autre constante de vitesse.
  
  La fonction utilise ces vitesses de reaction pour calculer le changement de concentration de fer, d'ions Fe2+, d'oxygene et d'eau au fil du temps  
  
  Les conditions initiales sont :
  
  concentration du Fer = 1 mol/m^3
  
  concentration des ions Fe2+ = 0 mol/m^3
  
  concentration d'oxygene= 1 mol/m^3
  
  concentration de l'eau= 0 mol/m^3
  
  avec les concentrations de vitesse de 0.01 et 0.02 respectivement:
  
  
  ![download](https://user-images.githubusercontent.com/125261904/231407468-63b83999-7980-40ab-b114-54884f0c0a55.png)
  
  Avec les concentrations de vitesse de 0.08 et 0.06 respectivement:
  
  ![download](https://user-images.githubusercontent.com/125261904/231417890-97a5b57e-e632-47e8-922b-494e1c8fef92.png)
  
  en changeant la concentration de l'eau en 0.5 mol/m^3, on obtient:
  
  ![download](https://user-images.githubusercontent.com/125261904/231418324-cd0fc7eb-a301-492b-84f1-18f2016825c5.png)


 On a voulu etudier le changement de concentration de l'oxygene et de la rouille a partir d'une reaction electrochimique appelee reaction de Butler-Volmer.
 
 Pour ca, on a utilise les taux de reaction anodique et cathodique en calculant leurs potentiels d'equilibre avec les formules suivantes:
 
 #insert pic of les equations Futur Lyna !!!!
 
 La simulation est effectuee en utilisant la fonction solve_ivp de NumPy pour resoudre les equations differentielles et les resultats sont traces a l'aide de Matplotlib.
 
 En initialisant les concentrations de l'oxygene,de la rouille et de l'eau a 1 mol/m^3 , 0 mol/m^3 et a 55.5 mol/m^3 respectivement et en mettant la temperature a 298° K, on obtient ces graphes :


  ![download](https://user-images.githubusercontent.com/125261904/231439849-4817d0e2-c67e-4732-a0de-d21e1122680c.png)
  
  en mettant les concentrations a 0.5 mol/m^3 chacune , on a :
  
  ![download](https://user-images.githubusercontent.com/125261904/231440556-ecdfdfe2-d451-496b-b5ba-e167889f6477.png)
  
  en augmentant la temperature jusqu'a 500° K, on a:
  
  ![download](https://user-images.githubusercontent.com/125261904/231441926-c0517e69-d5d9-43f7-86db-fe1b8f985b63.png)
  
  en mettant les concentrations de l'oxygene et de la rouille,a 0.7 mol/m^3 et a 0.3 mol/m^3 respectivement, et en augmentant la concentration de l'eau a 100 mol/m^3 on a comme resultat :
  
  ![download](https://user-images.githubusercontent.com/125261904/231443198-0cc5e5f8-a485-4e33-8032-7250b4c365d0.png)

On a aussi trace les densites de courant anodique et cathodique en fonction du potentiel:

![download](https://user-images.githubusercontent.com/125261904/231443740-377d8d90-343a-41b5-a0f6-7351ba59b245.png)


  
  

  
  
  
  
   
   
   
  
  

  
  
  
  
