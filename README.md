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


   
  On a ensuite voulu modeliser les reactions anodiques et cathodiques en utilisant la methode de Butler-Volmer.
  
  
   
   
   
  
  

  
  
  
  
