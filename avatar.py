#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes create a console-based avatar-creating tool.
#              The program allows the user to build a custom avatar or select from one of
#              three pre-designed ones (Jeff, Chris, and Jane).
#

def jeff():
    """
    it prints out an avatar named Jeff
    :return: the printed-out form of the avatar named Jeff
    """
    print()
    print("""       ~-~       
     /-~-~-\     
 ___/_______\___ 
    |'''''''|    
    | 0   0 |    
    |   V   |     
    |  ~~~  |     
     \_____/     
      |-X-|      
 0====|---|====0
      |-X-|      
      |-X-|      
      |-X-|      
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
#HHH#       #HHH# """)


def jane():
    """
    it prints out an avatar named Jane
    :return: the printed-out form of the avatar named Jane
    """
    print()
    print("""       ~-~       
     /-~-~-\     
    /_______\___ 
   "|\"\"\"\"\"\"\"|\"    
   "| *   * |"   
   "|   V   |"    
   "|  ~~~  |"    
   " \_____/ "   
 0TTTT|---|TTTT0
      |-X-|      
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
   ///     \\\\\\
<|||>       <|||>""")


def chris():
    """
    it prints out an avatar named Chris
    :return: the printed-out form of the avatar named Chris
    """
    print()
    print("""       ~-~       
     /-~-~-\     
    /_______\    
    |\'\'\'\'\'\'\'|    
    | U   U |    
    |   V   |     
    |  ~~~  |     
     \_____/     
      |-X-|      
 0WWWW|---|WWWW0
      |-X-|      
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
   ///     \\\\\\
  ///       \\\\\\
<>-<>       <>-<>""")


def hat_style(hat):
    """
    prints out a hat with the specified position asked by the user
    :param hat: is a string input which specifies if the hat should be looking to
    the left, right, both sides or front
    :return: the string hat with the specified position
    """
    print()
    if hat == 'left':
        print("""       ~-~       
     /-~-~-\     
 ___/_______\    """)
    elif hat == 'right':
        print("""       ~-~       
     /-~-~-\     
    /_______\___ """)
    elif hat == 'both':
        print("""       ~-~       
     /-~-~-\     
 ___/_______\___ """)
    else:
        print("""       ~-~       
     /-~-~-\     
    /_______\    """)


def hair_and_eyes(hair_length, eyes):
    """
    prints out the head of the avatar with the eyes as that of the input provided and
    either long or short hair
    :param hair_length: the string (True/False) determines if the hair
    should be long (True) or not (False)
    :param eyes: the string determining the exact character that is used for the eyes
    :return: the printed out version of the head with its eyes and either long or short hair
    """
    if hair_length == 'True':
        print('   "|"""""""|"    ')
        print('   "| ' + eyes + '   ' + eyes + ' |"   ')
        print('   "|   V   |"    ')
        print('   "|  ~~~  |"    ')
        print('   " \_____/ "    ')
    else:
        print("    |'''''''|    ")
        print('    | ' + eyes + '   ' + eyes + ' |   ')
        print('    |   V   |    ')
        print('    |  ~~~  |    ')
        print('     \_____/     ')


def arm_style(arms):
    """
    prints out the arm of the avatar using the input provided
    :param arms: the string character provided by the user
    :return: the printed form of the arm of the avatar using the character provided by the user
    """
    index = 0
    arm = ' 0'
    while index < 4:
        arm += arms
        index += 1
    arm += '|---|'
    index = 0
    while index < 4:
        arm += arms
        index += 1
    arm += '0'
    print(arm)


def torso(torso_height):
    """
    prints out the torso of the avatar of a particular length which is provided by the user
    :param torso_height: the integer that determines the length of the torso
    :return: the printed out version of the whole torso
    """
    index = 0
    while index < torso_height:
        print('      |-X-|      ')
        index += 1


def legs_and_shoes(leg_length, shoes):
    """
    prints out the legs and shoes of the avatar by using the inputs provided by the user
    :param leg_length: the integer that determines the length of the legs
    :param shoes: the string with the length of five that determines the type of the shoes
    :return: the ready version of the legs and shoes of the avatar
    """
    print('      HHHHH      ')
    index = 0
    left_leg = '///'
    right_leg = '\\\\\\'
    middle_space = 1
    while index < leg_length:
        print(' ' * (5 - index) + left_leg + ' ' * middle_space + right_leg)
        index += 1
        middle_space += 2
    print(shoes + ' ' * 7 + shoes)


def main():
    print('----- AVATAR -----')
    mode = input('Select an Avatar or create your own:\n')
    while mode != 'exit' and mode != 'Jeff' and mode != 'custom' \
            and mode != 'Jane' and mode != 'Chris':
        mode = input('Select an Avatar or create your own:\n')
    if mode == 'exit':
        return
    elif mode == 'Jane':
        jane()
    elif mode == 'Jeff':
        jeff()
    elif mode == 'Chris':
        chris()
    else:
        print('Answer the following questions to create a custom avatar')
        hat = input('Hat style ?\n')
        eyes = input('Character for eyes ?\n')
        hair_length = input('Long hair (True/False) ?\n')
        arms = input('Arm style ?\n')
        torso_height = int(input('Torso length ?\n'))
        leg_length = int(input('Leg length (1-4) ?\n'))
        shoes = input('Shoe look ?\n')
        hat_style(hat)
        hair_and_eyes(hair_length, eyes)
        arm_style(arms)
        torso(torso_height)
        legs_and_shoes(leg_length, shoes)


main()
